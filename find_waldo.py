import argparse
import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that finds a template in an image')
    parser.add_argument('img', help='The image to search')
    parser.add_argument('tmp', help='The template to search for')

    args = parser.parse_args()

    img_rgb = cv2.imread(args.img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(args.tmp,0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 5)

    cv2.imwrite('res.png',img_rgb)
    cv2.imshow("res.png", img_rgb)

    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()