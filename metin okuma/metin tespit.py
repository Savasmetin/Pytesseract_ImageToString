import cv2
import numpy as np
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

src_path = ""

def metintespitet(img_name):
    img = cv2.imread(img_name)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imwrite("gurultusuz.png",img)
    sonuc = pytesseract.image_to_string(Image.open("gurultusuz.png"),lang="tur")
    with open("metinler.txt","w") as file:
        file.write(sonuc)
    return sonuc



print(metintespitet("ekraniki.png"))


