import cv2
import datetime #For printing date time 

cap = cv2.VideoCapture(0)

print( cap.get(cv2.CAP_PROP_FRAME_WIDTH) )
print( cap.get(cv2.CAP_PROP_FRAME_HEIGHT) )

#Setting Parameters of Height and Width ( 3=width, 4=height)
# cap.set(3, 1280)
# cap.set(4, 720)

# print(cap.get(3))
# print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        #text variable stores height and width of the video
        text = 'Width : ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))

        #datet variable stores current date and time
        datet = str( datetime.datetime.now() )

        frame = cv2.putText(frame, datet, (10, 50), font, 1, 
                            (0, 255, 255), 2, cv2.LINE_AA)

        # #grayscale camera window
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #opening camera
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):   #pressing q key to exit camera
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()