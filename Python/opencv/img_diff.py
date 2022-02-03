import cv2 as cv
import ocv_common as com


def main(cam_src=None):
    if cam_src == None:
        cam_src = 0
    cap = cv.VideoCapture(cam_src)

    c = 0
    key = 0
    run = True
    _, last_frame = cap.read()
    try:
        while run:
            c = c + 1
            has_frame, frame = cap.read()

            if has_frame:
                canny = None
                canny_hue = None
                if key <= 2:
                    canny = com.get_diff_canny(frame, last_frame)
                    canny_hue = com.color_base_motion(frame, last_frame, 0)
                elif key == 3:
                    canny = com.color_base_motion(frame, last_frame, 0)

                if canny_hue is not None:
                    selections_hue = com.get_selections(canny_hue)

                if canny is not None:
                    selections = com.get_selections(canny)

                frame_c = frame.copy() if key > 1 else canny.copy()

                for a in sorted(selections, reverse=True):
                    x, y, w, h = selections[a]
                    cv.rectangle(
                        frame_c,
                        (x, y),
                        (x + w, y + h),
                        color=(0, 255, 0),
                        thickness=2,
                    )

                for a in sorted(selections_hue, reverse=True):
                    x, y, w, h = selections_hue[a]
                    cv.rectangle(
                        frame_c,
                        (x, y),
                        (x + w, y + h),
                        color=(200, 0, 0),
                        thickness=4,
                    )

                selections = {}
                selections_hue = {}
                cv.imshow("main", frame_c)

                ## last frame
                last_frame = frame.copy()

            waitKey = cv.waitKey(1)
            if waitKey > 0:
                # print(waitKey, chr(waitKey))
                if waitKey in [ord(str(i)) for i in range(10)]:
                    print(f"{waitKey=}, {key}")
                    key = int(chr(waitKey))
                if waitKey == ord("q") or waitKey == 27:
                    run = False

    except KeyboardInterrupt as e:
        print("quiting")


if __name__ == "__main__":
    usr = pas = "aaa"
    ip = "192.168.50.175"
    port = "8080"
    ip_cam_url = f"http://{usr}:{pas}@{ip}:{port}/video"
    main()
    # main(ip_cam_url)
