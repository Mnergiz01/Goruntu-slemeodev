import cv2
import numpy as np


kamera=cv2.VideoCapture(0)#kameradan canlı görüntü alır
lower=np.array([160,155,85])  #kırmızının hsv aralıkları
upper=np.array([180,255,255])

while True:
    ret,goruntu=kamera.read()
    hsv=cv2.cvtColor(goruntu,cv2.COLOR_HSV2BGR) #renk uzayını hsv yapma
    maske=cv2.inRange(hsv,lower,upper) #maskeleme işlemi
    red=cv2.bitwise_and(goruntu,goruntu,mask=maske)




    cv2.imshow("Muzaffer ",goruntu) #görüntüyü gösterir
    cv2.imshow("maskeli görüntü ", maske)  #maskeli görüntüyü gösterir
    cv2.imshow("hsv görüntü ",hsv)  # görüntüyü hsv gösterir
    cv2.imshow("kirmizi ", red)  # kırmızı olan görüntüyü gösterir



    if cv2.waitKey(1) & 0xFF == ord ('q'):  #1ms de görüntüleri göster q ye basınca çık
        break




kamera.release()       #kamerayı sıfırlar
cv2.destroyAllWindows()  #pencereleri kapatır