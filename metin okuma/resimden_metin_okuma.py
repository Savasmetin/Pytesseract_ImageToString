import cv2
import numpy as np
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd= "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
kaynak_yolu=""
def metin_oku(img_yolu):
    img=cv2.imread(img_yolu)

    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    kernel=np.ones((1,1),np.uint8)
    img=cv2.erode(img,kernel,iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)


    cv2.imwrite(kaynak_yolu+'gurultusuz.png',img)

    sonuc=pytesseract.image_to_string(Image.open(kaynak_yolu+'gurultusuz.png'),lang='tur')
    return sonuc

print("---------------------------------")
print("metin okuma")
print("---------------------------------")
print(metin_oku('a2.png'))

print("---------------------------------")
print("tamamlandı")
