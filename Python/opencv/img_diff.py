from turtle import Turtle
import cv2 as cv


def get_diff(im1, im2):
    im1_g = cv.cvtColor(im1.copy(), cv.COLOR_BGR2GRAY)
    im2_g = cv.cvtColor(im2.copy(), cv.COLOR_BGR2GRAY)
    return cv.absdiff(im1_g, im2_g)


def get_hue_mask(hsv, value):
    if value < 0:
        value = 0
    if value > 255:
        value = 255

    hue = hsv[:, :, 0]
    _, th = cv.threshold(hue - value, 225, 255, cv.THRESH_BINARY)
    return th


def get_diff_canny(frame, last_frame):
    sub_frame = get_diff(frame, last_frame)
    sub_frame = cv.GaussianBlur(sub_frame, (11, 11), 100)
    _, mask = cv.threshold(sub_frame, 50, 255, cv.THRESH_BINARY)
    canny = cv.Canny(mask, 100, 200)
    return canny


def color_base_motion(im1, im2, hue_val):
    hsv1 = cv.cvtColor(im1, cv.COLOR_BGR2HSV_FULL)
    # hsv2 = cv.cvtColor(im2, cv.COLOR_BGR2HSV_FULL)

    th1 = get_hue_mask(hsv1, hue_val)
    # th2 = get_hue_mask(hsv2, hue_val)

    f_img1 = cv.bitwise_and(im1, im1, mask=th1)
    f_img2 = cv.bitwise_and(im2, im2, mask=th1)

    diff = get_diff(f_img1, f_img2)
    sub_frame = cv.GaussianBlur(diff, (11, 11), 100)
    _, mask = cv.threshold(sub_frame, 50, 255, cv.THRESH_BINARY)

    return cv.Canny(mask, 100, 200)


def get_selections(canny):
    ## get selection
    contours, _ = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    selections = {
        w * h: (x, y, w, h) for x, y, w, h in [cv.boundingRect(cnt) for cnt in contours]
    }

    return selections


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
                if key <= 2:
                    canny = get_diff_canny(frame, last_frame)
                elif key == 3:
                    canny = color_base_motion(frame, last_frame, 0)

                if canny is not None:
                    selections = get_selections(canny)

                frame_c = frame.copy() if key > 1 else canny.copy()

                for a in sorted(selections, reverse=True):
                    x, y, w, h = selections[a]
                    cv.rectangle(
                        frame_c,
                        (x, y),
                        (x + w, y + h),
                        color=(0, 255, 0),
                        thickness=3,
                    )

                selections = {}
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
