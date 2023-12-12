import cv2

def open_camera(camera_index=0):
    # Open the camera
    cap = cv2.VideoCapture(camera_index)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Loop to continuously capture frames from the camera
    while True:
        # Capture a single frame from the camera
        ret, frame = cap.read()

        # Check if the frame is captured successfully
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the captured frame in a window titled 'Camera Feed'
        cv2.imshow('Camera Feed', frame)

        # Break the loop if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Set the camera index (usually 0 for the default camera)
    camera_index = 0

    # Open the laptop camera and display the video stream
    open_camera(camera_index)
