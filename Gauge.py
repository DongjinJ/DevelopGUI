# pip install opencv-python
import cv2
import numpy as np
import time

def Stick_Gauge_Draw(img, center_x, center_y, width, height, value):
    base_Color = (240, 75, 140)
    end_Color = (9, 23, 237)
    background_Color = (115, 26, 48)
    scale_Color = (64, 64, 64)
    leftUpper_Point = [int(center_x - (width / 2) * 0.9), int(center_y - (height / 6))]
    rightUpper_Point = [int(center_x + (width / 2)),       int(center_y - (height / 6))]
    rightLower_Point = [int(center_x + (width / 2) * 0.9), int(center_y + (height / 6))]
    leftLower_Point = [int(center_x - (width / 2)),       int(center_y + (height / 6))]
    gaugePoint = np.array([leftUpper_Point, rightUpper_Point, rightLower_Point, leftLower_Point], np.int32)
    img = cv2.polylines(img, [gaugePoint], True, background_Color, 2)

    for i in range(10):
        upper_Point = [int((center_x - (width / 2) * 0.9) + (1.9 / 2 * width * i / 10)), int(center_y - (height / 6))]
        lower_Point = [int(center_x - (width / 2) + (1.9 / 2 * width * i / 10)),       int(center_y + (height / 6))]
        img = cv2.line(img, upper_Point, lower_Point, scale_Color, 1)
    
    
    
    if value != 0:
        current_Color = base_Color
        for i in range(0, value + 1):

            rightUpper_Point = [int(center_x - (width / 2) * 0.9 + (1.9 / 2 * width * (value / 100) * (i / value))), int(center_y - (height / 6))]
            rightLower_Point = [int(center_x - (width / 2) + (1.9 / 2 * width * (value / 100) * (i / value))), int(center_y + (height / 6))]
            gaugePoint = np.array([leftUpper_Point, rightUpper_Point, rightLower_Point, leftLower_Point], np.int32)
            img = cv2.fillConvexPoly(img, gaugePoint, current_Color)

            leftUpper_Point = rightUpper_Point
            leftLower_Point = rightLower_Point
            current_Color_B = int(base_Color[0] - (abs(end_Color[0] - base_Color[0]) * i / value))
            current_Color_G = int(base_Color[1] - (abs(end_Color[1] - base_Color[1]) * i / value))
            current_Color_R = int(base_Color[2] + (abs(end_Color[2] - base_Color[2]) * i / value))
            current_Color = (current_Color_B, current_Color_G, current_Color_R)


    

if __name__ == "__main__":
    HEIGHT = 400
    WIDTH = 400

    i = 0
    flag = False
    while True:
        img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
        Stick_Gauge_Draw(img, 100, 200, 200, 50, i)
        cv2.imshow(f'Test', img)

        if flag == True:
            i -= 1
        else:
            i += 1

        if i == 100:
            flag = True
        elif i == 0:
            flag = False
        
        time.sleep(0.1)
        

        if cv2.waitKey(1) & 0xFF == ord('x'):
            cv2.destroyAllWindows()
            break

        


    