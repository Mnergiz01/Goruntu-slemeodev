import cv2
import numpy as np

img=cv2.VideoCapture(0)

while True:
    ret, goruntu = img.read()
    gray = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

    equalized_image = cv2.equalizeHist(gray)
    ret, thresh = cv2.threshold(equalized_image, 30,255, cv2.THRESH_BINARY)
    cont, a = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# Belirli bir büyüklük eşiği (min_area_threshold)
    min_alan_threshold = 500

# Konturları çizme ve belirli büyüklükte olanları sayma
    contour_img = goruntu.copy()
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

        cv2.imshow("nesneler ", contour_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 1ms de görüntüleri göster q ye basınca çık
        break
# Belirli büyüklükteki nesne sayısını yazdır
    print(f'Toplam {min_alan_threshold} pikselin üzerinde olan Nesne Sayısı:', object_counter)

img.release()       #kamerayı sıfırlar
cv2.destroyAllWindows()