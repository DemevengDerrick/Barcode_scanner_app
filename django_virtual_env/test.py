import cv2
from pyzbar import pyzbar

def scan_barcode():
    # Initialize the video capture object
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use the pyzbar library to detect and decode barcodes
        barcodes = pyzbar.decode(gray)

        # Loop over detected barcodes
        for barcode in barcodes:
            # Extract barcode data
            barcode_data = barcode.data.decode("utf-8")

            # Draw a bounding box around the barcode
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the barcode data on the frame
            cv2.putText(frame, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow("Barcode Scanner", frame)

        # Check for 'q' key press to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to start scanning barcodes using the camera
scan_barcode()