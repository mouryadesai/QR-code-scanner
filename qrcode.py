import cv2
from pyzbar.pyzbar import decode
import webbrowser


cap = cv2.VideoCapture(0) # Open the camera

while True:
    ret, frame = cap.read() #Read the frame
    decoded_objects = decode(frame) #Decode any QR codes in the frame

    for obj in decoded_objects: #Draw a rectangle around the QR code and open the URL in a web browser
        if obj.type == "QRCODE":
            url = obj.data.decode("utf-8")
            cv2.rectangle(frame, obj.rect, (0, 255, 0), 2)
            webbrowser.open(url)

  
    cv2.imshow("QR Code Scanner", frame) #Display the frame

    
    if cv2.waitKey(1) & 0xFF == ord('q'): #Quit if the user presses 'q'
        break


cap.release()
cv2.destroyAllWindows() #Release the camera and close the window
