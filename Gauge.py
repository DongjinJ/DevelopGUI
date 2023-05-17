# pip install opencv-python
import cv2
import numpy as np

def Gauge_Draw(img, center_x, center_y, size, value):
    leftUpper_Point = [int(center_x - (size / 2) * 0.9), int(center_y - (size / 6))]
    rightUpper_Point = [int(center_x + (size / 2)),       int(center_y - (size / 6))]
    rightLower_Point = [int(center_x + (size / 2) * 0.9), int(center_y + (size / 6))]
    leftLower_Point = [int(center_x - (size / 2)),       int(center_y + (size / 6))]
    gaugePoint = np.array([leftUpper_Point, rightUpper_Point, rightLower_Point, leftLower_Point], np.int32)
    img = cv2.polylines(img, [gaugePoint], True, (255, 255, 255), 2)
    rightUpper_Point = [int(center_x - (size / 2) * 0.9 + (1.9 / 2 * size * (value / 100))), int(center_y - (size / 6))]
    rightLower_Point = [int(center_x - (size / 2) + (1.9 / 2 * size * (value / 100))), int(center_y + (size / 6))]
    gaugePoint = np.array([leftUpper_Point, rightUpper_Point, rightLower_Point, leftLower_Point], np.int32)
    img = cv2.fillConvexPoly(img, gaugePoint, (255, 255, 255))

    

if __name__ == "__main__":
    HEIGHT = 400
    WIDTH = 400
    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
    Gauge_Draw(img, 100, 200, 100, 25)
    cv2.imshow('Test1', img)
    Gauge_Draw(img, 100, 200, 100, 50)
    cv2.imshow('Test2', img)
    Gauge_Draw(img, 100, 200, 100, 75)
    cv2.imshow('Test3', img)
    Gauge_Draw(img, 100, 200, 100, 100)
    cv2.imshow('Test4', img)

    cv2.waitKey(0)