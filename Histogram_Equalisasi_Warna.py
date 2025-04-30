import cv2
import numpy as np

#Baca gambar
img = cv2.imread('img/image_1.jpg')

# Perikasa apakah gambar terbaca
if img is None:
    print('Could not read image')
    exit()

# Resize gambar
img = cv2.resize(img, (640, 480))

# Koversi dari BGR ke YCrCb
ycc = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

# Pisahkan channel
y, cr, cb = cv2.split(ycc)

# Histogram Equalisasi pada channel Y
y_eq = cv2.equalizeHist(y)

# Gabungkan channel kembali
ycc_eq = cv2.merge([y_eq, cr, cb])

# Koversi dari YCrCb ke BGR
img_eq = cv2.cvtColor(ycc_eq, cv2.COLOR_YCR_CB2BGR)

# Tampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()