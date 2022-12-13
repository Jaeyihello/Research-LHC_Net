# 영상 및 이미지 전처리
# 영상 입력 path

import cv2

video_file = "Test_Video/Anger/Anger1.mp4"     # 동영상 파일 경로
save_file = "Test_Data/Anger/Anger1/Img"       # 파일 저장 경로

cap = cv2.VideoCapture(video_file) # 동영상 캡쳐 객체 생성  
ind = 0
if cap.isOpened():                 # 캡쳐 객체 초기화 확인
    while True:
        ret, img = cap.read()      # 다음 프레임 읽기      
        if ret:                     # 프레임 읽기 정상
            cv2.imshow(video_file, img) # 화면에 표시
            dst = img[200:650, 700:1150].copy()
            cv2.imshow("img", img)
            cv2.imshow("dst", dst)

            cv2.imwrite(save_file + str(ind) +'.jpg', dst)  #파일로 저장, 포맷은 확장에 따름
            cv2.waitKey(25)            # 25ms 지연(40fps로 가정)   
            ind += 1
        else:                       # 다음 프레임 읽을 수 없슴,
            break                   # 재생 완료
else:
    print("can't open video.")      # 캡쳐 객체 초기화 실패
cap.release()                       # 캡쳐 자원 반납
cv2.destroyAllWindows()
