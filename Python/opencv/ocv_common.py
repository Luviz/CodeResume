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
