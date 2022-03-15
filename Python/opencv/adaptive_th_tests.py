import cv2 as cv
import ocv_common as cvc


def main(cam_src=None):
    if cam_src == None:
        cam_src = 0
    cap = cv.VideoCapture(cam_src)

    c = 0
    key = 0
    run = True
    max_val = 255
    block_size = 11
    constant = 28
    useCanny = False
    useBlur = False
    useContours = False
    _, last_frame = cap.read()

    try:
        while run:
            c = c + 1
            has_frame, frame = cap.read()
            if block_size < 2:
                block_size = 3

            if has_frame:
                g_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                c_frame = cv.adaptiveThreshold(
                    g_frame,
                    max_val,
                    cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv.THRESH_BINARY,
                    block_size,
                    constant,
                )

                if useBlur:
                    c_frame = cv.GaussianBlur(c_frame, (3, 3), 5)

                if useCanny:
                    c_frame = cv.Canny(
                        c_frame,
                        255,
                        255,
                    )

                selections = cvc.get_selections(c_frame)
                c_frame = cv.cvtColor(c_frame, cv.COLOR_GRAY2BGR)

                if useContours:
                    for a in sorted(selections, reverse=True)[:10]:
                        x, y, w, h = selections[a]
                        cv.rectangle(
                            c_frame,
                            (x, w + x),
                            (y, h + y),
                            color=(100, 200, 100),
                            thickness=1,
                        )

                cv.putText(
                    img=c_frame,
                    text=f"{max_val = } | {block_size = } | {constant = }",
                    org=(30, 40),
                    fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    color=(0, 0, 200),
                    fontScale=1,
                    thickness=3,
                )

                cv.imshow("main", c_frame)
                ## last frame
                last_frame = frame.copy()

            waitKey = cv.waitKey(1)
            if waitKey > 0:
                # print(waitKey, chr(waitKey))
                if waitKey in [ord(str(i)) for i in range(10)]:
                    print(f"{waitKey=}, {key}")
                    key = int(chr(waitKey))
                elif waitKey == ord("q") or waitKey == 27:
                    run = False
                # max val
                elif waitKey == ord("u"):
                    max_val += 5
                elif waitKey == ord("j"):
                    max_val -= 5
                # block size
                elif waitKey == ord("i"):
                    block_size += 2
                elif waitKey == ord("k"):
                    block_size -= 2
                elif waitKey == ord("o"):
                    constant += 1
                elif waitKey == ord("l"):
                    constant -= 1
                elif waitKey == ord("c"):
                    useCanny = not useCanny
                elif waitKey == ord("b"):
                    useBlur = not useBlur
                elif waitKey == ord("v"):
                    useContours = not useContours

    except KeyboardInterrupt as e:
        print("quiting")


if __name__ == "__main__":
    usr = pas = "aaa"
    ip = "192.168.50.175"
    port = "8080"
    ip_cam_url = f"http://{usr}:{pas}@{ip}:{port}/video"
    # main()
    main(ip_cam_url)
