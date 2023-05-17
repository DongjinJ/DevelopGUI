# pip install opencv-python
import cv2
import numpy as np

def Gauge_Draw(img, center_x, center_y, size, value):
    base_Color = (240, 75, 140)
    end_Color = (9, 23, 237)
    background_Color = (128, 128, 128)
    leftUpper_Point = [int(center_x - (size / 2) * 0.9), int(center_y - (size / 6))]
    rightUpper_Point = [int(center_x + (size / 2)),       int(center_y - (size / 6))]
    rightLower_Point = [int(center_x + (size / 2) * 0.9), int(center_y + (size / 6))]
    leftLower_Point = [int(center_x - (size / 2)),       int(center_y + (size / 6))]
    gaugePoint = np.array([leftUpper_Point, rightUpper_Point, rightLower_Point, leftLower_Point], np.int32)
    img = cv2.polylines(img, [gaugePoint], True, background_Color, 2)
    current_Color = base_Color
    for i in range(0, value + 1):
        
        rightUpper_Point = [int(center_x - (size / 2) * 0.9 + (1.9 / 2 * size * (value / 100) * (i / value))), int(center_y - (size / 6))]
        rightLower_Point = [int(center_x - (size / 2) + (1.9 / 2 * size * (value / 100) * (i / value))), int(center_y + (size / 6))]
        gaugePoint = np.array([leftUpper_Point, rightUpper_Point, rightLower_Point, leftLower_Point], np.int32)
        img = cv2.fillConvexPoly(img, gaugePoint, current_Color)

        leftUpper_Point = rightUpper_Point
        leftLower_Point = rightLower_Point
        current_Color_B = int(base_Color[0] - (abs(end_Color[0] - base_Color[0]) * i / value))
        current_Color_G = int(base_Color[1] - (abs(end_Color[1] - base_Color[1]) * i / value))
        current_Color_R = int(base_Color[2] + (abs(end_Color[2] - base_Color[2]) * i / value))
        current_Color = (current_Color_B, current_Color_G, current_Color_R)
        print(current_Color, value, i)


    

if __name__ == "__main__":
    HEIGHT = 400
    WIDTH = 400
    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
    Gauge_Draw(img, 100, 200, 100, 25)
    cv2.imshow('Test1', img)

    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
    Gauge_Draw(img, 100, 200, 150, 50)
    cv2.imshow('Test2', img)

    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
    Gauge_Draw(img, 100, 200, 200, 75)
    cv2.imshow('Test3', img)

    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
    Gauge_Draw(img, 100, 200, 250, 100)
    cv2.imshow('Test4', img)

    cv2.waitKey(0)