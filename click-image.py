import cv2

def capture_image(camera_index=0, output_path='captured_image.jpg'):
    # Open the camera
    cap = cv2.VideoCapture(camera_index)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame from the camera
    ret, frame = cap.read()

    # Check if the frame is captured successfully
    if not ret:
        print("Error: Failed to capture image.")
        return

    # Save the captured frame to a file
    cv2.imwrite(output_path, frame)

    # Release the camera
    cap.release()

    # Display a message indicating that the image has been captured and saved
    print(f"Image captured and saved to {output_path}")

if __name__ == "__main__":
    # Set the camera index (usually 0 for the default camera)
    camera_index = 0

    # Set the output path for the captured image
    output_path = 'captured_image.jpg'

    # Capture the image using the default camera index and save it to the specified output path
    capture_image(camera_index, output_path)
