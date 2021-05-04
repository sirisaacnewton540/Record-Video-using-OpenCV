import cv2
import datetime

cap = cv2.VideoCapture(0)
forcc = cv2.VideoWriter_fourcc(*'XVID')
rec = cv2.VideoWriter('rec.mp4',forcc,20,(640,480))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
while(True):
    ret, frame=cap.read()
    
    if ret ==True:
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        dt = str(datetime.datetime.now())
        frame = cv2.putText(frame,dt,(10,50),font,1,(0,255,255),3)
        rec.write(frame)
        cv2.imshow('frame',frame)
    
        k=cv2.waitKey(1) & 0xFF

        if k==ord('q'):
            break
    else:
        break
cap.release()
#rec.release()
cv2.destroyAllWindows()
