import cv2 as cv

print(cv.__version__)
# cap = cv.VideoCapture(0)
cap = cv.VideoCapture("http://aaa:aaa@192.168.50.175:8080/video")


print("aa")
while True:
    rat, frame = cap.read()
    if rat:
        print("bb", rat)
        cv.imshow("canny", frame)
        print("cc")
    key = cv.waitKey(1)
    if key == ord("q"):
        break
