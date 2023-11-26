import cv2
import numpy as np

img = cv2.imread("makarna.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equalized_image = cv2.equalizeHist(gray)
ret, thresh = cv2.threshold(equalized_image, 30,255, cv2.THRESH_BINARY)
cont, a = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow("Cizim", img)
cv2.imshow("eşikleme", thresh)
cv2.imshow("histogram", equalized_image)
#drawcontours ile kare kare değil direkt çizim yapar kenarlarında
#cv2.drawContours(img, cont, -1, (0, 255, 0), 2)

#cv2.imshow("Cizim", img)
#cv2.waitKey(0)
# Konturları çizme ve sayma
# Belirli bir büyüklük eşiği (min_area_threshold)
min_alan_threshold = 500

# Konturları çizme ve belirli büyüklükte olanları sayma
contour_img = img.copy()
object_counter = -1

for contour in cont:
    # Her bir kontur için alanı hesapla
    alan = cv2.contourArea(contour)

    # Belirli bir alan eşiğini karşılayan nesneleri say
    if alan > min_alan_threshold:
        # Her bir kontur için dikdörtgen çevresini al
        x, y, w, h = cv2.boundingRect(contour)

        # Dikdörtgeni çiz
        cv2.rectangle(contour_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Nesne sayısını artır
        object_counter += 1

# Belirli büyüklükteki nesne sayısını yazdır
print(f'Toplam {min_alan_threshold} pikselin üzerinde olan Nesne Sayısı:', object_counter)

# Görüntüyü gösterme
cv2.imshow("nesneler ", contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()