import cv2

#capture variable
cap = cv2.VideoCapture(0)

#output variable for saving frame from camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#60.0 is default fps, I've used 100 for fast vid | 640 X 480 is dim
out = cv2.VideoWriter('output.avi', fourcc, 100.0, (640,480))

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)

        #grayscale camera window
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #opening camera
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):#pressing q key to exit camera
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()