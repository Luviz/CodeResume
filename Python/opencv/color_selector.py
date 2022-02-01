import cv2 as cv
from matplotlib.pyplot import prism


def main(cam_src=None):
    if cam_src == None:
        cam_src = 0
    cap = cv.VideoCapture(cam_src)

    c = 0
    key = 2
    run = True
    frm = 0  # 150
    rect = None
    x_i = 1

    try:
        while run:
            _, frame = cap.read()
            if key == 1:
                cv.imshow("frame", frame)
            else:
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV_FULL)
                hue = hsv[:, :, 0]
                _, th0 = cv.threshold(hue - frm, 225, 255, cv.THRESH_BINARY)
                f = cv.bitwise_and(frame, frame, mask=th0)

                cv.imshow("frame", f)

            waitKey = cv.waitKey(1)
            if waitKey > 0:
                # print(waitKey, chr(waitKey))
                if waitKey in [ord(str(i)) for i in range(10)]:
                    print(f"{waitKey=}, {key}")
                    key = int(chr(waitKey))
                if waitKey == ord("o"):
                    frm = frm + 5
                    if frm > 255:
                        frm = 255
                    print(f"{frm = }")
                if waitKey == ord("l"):
                    frm = frm - 5
                    if frm < 0:
                        frm = 0
                    print(f"{frm = }")
                if waitKey == ord("i"):
                    x_i = x_i + 2
                    print(f"{x_i = }")
                if waitKey == ord("k"):
                    x_i = x_i - 2
                    if x_i < 1:
                        x_i = 1
                    print(f"{x_i = }")

                if waitKey == ord("q") or waitKey == 27:
                    run = False

    except KeyboardInterrupt as e:
        print("quiting")


def getHue(start: int, offset: int):
    rest = 255 % (start + offset)
    if start + offset // 255:
        pass


if __name__ == "__main__":
    usr = pas = "aaa"
    ip = "192.168.50.175"
    port = "8080"
    ip_cam_url = f"http://{usr}:{pas}@{ip}:{port}/video"
    main(ip_cam_url)
