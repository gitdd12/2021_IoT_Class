import cv2

img = cv2.imread('IU.jpg')

img = cv2.resize(img, (1000, 800))

#흑백 이미지로 변환하기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('IU', img)
cv2.imshow('IU_GRAY', gray)
# ENTER : 13, ESC: 27, A : 65, a : 97
while True:
    if cv2.waitKey(0) == 13:
        break
cv2.imwrite('IU_GRAY.jpg', gray)
cv2.destroyAllWindows()

