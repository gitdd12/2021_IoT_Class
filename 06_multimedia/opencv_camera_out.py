import cv2

#카메라 장치 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()


#fourcc(four character code) : DIVX(avi), MP4V(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #('D','I','V','X')
              #파일명     #위에서 정의한거        #프레임    # 프레임 사이즈
out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))



#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
     break

    cv2.imshow('frame', frame)
    out.write(frame)
    #1000 -> 1초, 10->0.01초
    if cv2.waitKey(10) == 13:
        break
cap.release()
out.release()
cv2.destroyAllWindows()