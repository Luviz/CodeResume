import cv2 as cv
import ocv_common as cvc


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
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV_FULL)

                hsv = cv.blur(hsv, (11, 11))

                # 0 = red; 100 = green; 190 blue
                color_masks = [
                    cvc.get_hue_mask(hsv, hue_start) for hue_start in [0, 100, 190]
                ]

                color_cannies = [cv.Canny(m, 100, 200) for m in color_masks]
                frame_c = frame.copy()

                for ix, color_canny in enumerate(color_cannies):
                    selections = cvc.get_selections(color_canny)
                    for a in sorted(selections, reverse=True)[:2]:
                        x, y, w, h = selections[a]
                        if ix == 0:
                            color = (0, 0, 255)
                        elif ix == 1:
                            color = (0, 255, 0)
                        elif ix == 2:
                            color = (255, 0, 0)
                        else:
                            color = (255, 255, 255)

                        cv.rectangle(
                            frame_c,
                            (x, y),
                            (x + w, y + h),
                            color=color,
                            thickness=2,
                        )

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
    # main()
    main(ip_cam_url)
