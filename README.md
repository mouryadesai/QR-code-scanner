# QR-code-scanner

The program uses the ''cv2.VideoCapture()'' function to open the default camera, and then runs a while loop to continuously read frames from the camera using the "cap.read()" method.

The "decode()" function from the PyZbar library is used to decode any QR codes in the frame. If a QR code is detected, the program extracts the URL from the code using the "obj.data" property, and then draws a green rectangle around the code using the "cv2.rectangle()" method.

Finally, the program opens the extracted URL in the default web browser using the "webbrowser.open()" method.

The program also displays the captured frame in a window using the "cv2.imshow()" method. 

The loop runs until the user presses the 'q' key, which breaks the loop, and the program releases the camera using the cap.release() method and closes the window using the "cv2.destroyAllWindows()" method.
