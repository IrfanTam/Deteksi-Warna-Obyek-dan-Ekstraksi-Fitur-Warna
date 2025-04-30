import cv2

#Baca gambar
img = cv2.imread('img/image_1.jpg')

# Perikasa apakah gambar terbaca
if img is None:
    print('Could not read image')
    exit()

# Resize gambar
img = cv2.resize(img, (640, 480))

# Ubah gambar menjadi grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Lakukan histogram equalization
hist_equalized_image = cv2.equalizeHist(gray_image)

# Tampilkan hasil
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Histogram Equalized Image", cv2.WINDOW_NORMAL)

cv2.imshow("Original Image", gray_image)
cv2.imshow("Histogram Equalized Image", hist_equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
