import cv2

# xml 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

#카메라 장치 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
     break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    #1000 -> 1초, 10->0.01초
    if cv2.waitKey(10) == 13:
        break
cap.release()
cv2.destroyAllWindows()
