# pip install opencv-python
import cv2
import numpy as np
import time
import math

def Stick_Gauge_Draw(img, center_x, center_y, width, height, value, text):
    base_Color = (240, 75, 140)
    end_Color = (9, 23, 237)
    background_Color = (115, 26, 48)
    scale_Color = (64, 64, 64)
    
    leftUpper_Point = [int(center_x - (width / 2) * 0.9), int(center_y - (height / 6))]
    rightUpper_Point = [int(center_x + (width / 2)),       int(center_y - (height / 6))]
    rightLower_Point = [int(center_x + (width / 2) * 0.9), int(center_y + (height / 6))]
    leftLower_Point = [int(center_x - (width / 2)),       int(center_y + (height / 6))]
    
    current_Color = base_Color
    if value != 0:
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

    leftUpper_Point = [int(center_x - (width / 2) * 0.9), int(center_y - (height / 6))]
    rightUpper_Point = [int(center_x + (width / 2)),       int(center_y - (height / 6))]
    rightLower_Point = [int(center_x + (width / 2) * 0.9), int(center_y + (height / 6))]
    leftLower_Point = [int(center_x - (width / 2)),       int(center_y + (height / 6))]
    gaugePoint = np.array([leftUpper_Point, rightUpper_Point, rightLower_Point, leftLower_Point], np.int32)

    text_Point = (leftUpper_Point[0], leftUpper_Point[1] - 10)
    cv2.putText(img, str(text), text_Point, cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
    img = cv2.polylines(img, [gaugePoint], True, background_Color, 2)
    

    for i in range(10):
        upper_Point = [int((center_x - (width / 2) * 0.9) + (1.9 / 2 * width * i / 10)), int(center_y - (height / 6))]
        lower_Point = [int(center_x - (width / 2) + (1.9 / 2 * width * i / 10)),       int(center_y + (height / 6))]
        img = cv2.line(img, upper_Point, lower_Point, scale_Color, 1)
    
    
    
def Arc_Gauge_Draw(img, center_x, center_y, size, value, text):
    base_Color = (240, 75, 140)
    end_Color = (9, 23, 237)
    background_Color = (115, 26, 48)
    scale_Color = (64, 64, 64)

    thick = 15
    inner_Radius = size - thick
    outer_Radius = size

    
    current_Color = base_Color

    text_Size = cv2.getTextSize(str(text), cv2.FONT_HERSHEY_DUPLEX, 0.8, 1)[0]
    text_Point = (int(center_x - text_Size[0] / 2), int(center_y + text_Size[1] / 2))
    
    cv2.putText(img, str(text), text_Point, cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
    target = int(135 + (270 * value / 100))
    innerPoint = []
    outerPoint = []

    # for i in range(135, 406):
    #     theta = math.pi * (i / 180)

    #     p1 = [int((inner_Radius * math.cos(theta)) + center_x), int((inner_Radius * math.sin(theta)) + center_y)]
    #     innerPoint.append(p1)
    #     p3 = [int((outer_Radius * math.cos(theta)) + center_x), int((outer_Radius * math.sin(theta)) + center_y)]
    #     outerPoint.append(p3)


    #     if ((i - 135) % 27 == 0) and (i != 135):
    #         totalPoint = []
    #         reversed_outerPoint = list(reversed(outerPoint))
    #         totalPoint = innerPoint + reversed_outerPoint
    #         coverPoint = np.array([totalPoint], np.int32)
    #         img = cv2.polylines(img, [coverPoint], True, background_Color, 2)


    for i in range(135, 406):
        theta = math.pi * (i / 180)
        nextTheta = math.pi * ((i + 1) / 180)
        p1 = [int((inner_Radius * math.cos(theta)) + center_x), int((inner_Radius * math.sin(theta)) + center_y)]
        innerPoint.append(p1)
        p2 = [int((inner_Radius * math.cos(nextTheta)) + center_x), int((inner_Radius * math.sin(nextTheta)) + center_y)]
        p3 = [int((outer_Radius * math.cos(theta)) + center_x), int((outer_Radius * math.sin(theta)) + center_y)]
        outerPoint.append(p3)
        p4 = [int((outer_Radius * math.cos(nextTheta)) + center_x), int((outer_Radius * math.sin(nextTheta)) + center_y)]

        if i <= target:
            gaugePoint = np.array([p1, p2, p4, p3], np.int32)
            img = cv2.fillConvexPoly(img, gaugePoint, current_Color)
            portion = (i - 135) / 270
            current_Color_B = int(base_Color[0] - (abs(end_Color[0] - base_Color[0]) * portion))
            current_Color_G = int(base_Color[1] - (abs(end_Color[1] - base_Color[1]) * portion))
            current_Color_R = int(base_Color[2] + (abs(end_Color[2] - base_Color[2]) * portion))
            current_Color = (current_Color_B, current_Color_G, current_Color_R)

        if ((i - 135) % 27 == 0) and (i != 135):
            totalPoint = []
            reversed_outerPoint = list(reversed(outerPoint))
            totalPoint = innerPoint + reversed_outerPoint
            coverPoint = np.array([totalPoint], np.int32)
            img = cv2.polylines(img, [coverPoint], True, background_Color, 2)

    

if __name__ == "__main__":
    HEIGHT = 400
    WIDTH = 400

    i = 0
    flag = False
    while True:
        img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
        Stick_Gauge_Draw(img, 100, 200, 200, 50, i, i)
        Arc_Gauge_Draw(img, 300, 200, 50, i, i)
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

        


    