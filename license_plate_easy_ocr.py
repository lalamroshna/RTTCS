import numpy as np
import os 
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from matplotlib import pyplot as plt
import cv2
import imutils
import easyocr
import re

def license_plate_detection(cropped_images):
    reader = easyocr.Reader(['en'])  #we’ve set the language as ‘en’ meaning English. 
    license_plate=r'([A-Za-z][A-Za-z][0-9][0-9][A-Za-z][A-Za-z][0-9][0-9][0-9][0-9])'    #pattern for Indian license plates
    print("Number Plate detected:")
    for file_path in cropped_images.values():
        img = cv2.imread(file_path, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
        # Read text from image
        result =reader.readtext(gray,detail=0,paragraph=True) 
        #detected_result=result[0].replace(" ","")   #remove unneccesary spaces from detected plate
        if(len(result)>1):
            result[1] = result[1][:0] + 'G' + result[1][0+1:]
            result[1] = result[1].upper()
            result[1] = result[1].replace(" ","") 
            print(result)
            ans=result[1]
        else:
            result[0] = result[0][:0] + 'G' + result[0][0+1:]
            result[0] = result[0].upper()
            result[0] = result[0].replace(" ","") 
            print(result)   # shows detected license plate
            ans=result[0]
        if re.search(license_plate,ans):
            text = result[0][-2]
            font = cv2.FONT_HERSHEY_SIMPLEX
            res = cv2.putText(img, text=text, org=(1,10), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
            plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
            plt.show()

if __name__ == '__main__':
    try:
        license_plate_detection()
    except SystemExit:
        pass
