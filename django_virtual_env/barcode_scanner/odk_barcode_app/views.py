from django.http import HttpResponse
from django.template import loader
from pyzbar import pyzbar
import cv2
import requests

def ona_connector(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def scanner(request):
    template = loader.get_template('scanner.html')
    # Open the camera
    cap = cv2.VideoCapture(0)

    barcode_data = "No barcode found."

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Decode barcodes from the grayscale image
        barcodes = pyzbar.decode(gray)

        # Loop over detected barcodes
        for barcode in barcodes:
            # Extract barcode data
            # Draw a bounding box around the barcode
            
            barcode_data = barcode.data.decode("utf-8")

            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the barcode data on the frame
            cv2.putText(frame, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            break  # Exit the loop after the first barcode is detected

        # Check for 'q' key press to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.imshow("Scanner", frame)
        cv2.waitKey(1)

    # Release the camera and clean up
    cap.release()
    cv2.destroyAllWindows()

    context = {'barcode': barcode_data}

    # Display the barcode data in the browser using the template
    return HttpResponse(template.render(context, request))

def display_data(request):
    template = loader.get_template('record.html')
    rq = requests.get("https://esurv.afro.who.int/api/v1/data/8604.json", auth=("gis_blueline", "G1sb!ue")).json()

    for record in rq:
        if record['epid_num'] == "ENV-ETH-SOM-FAF-SAG-17-001":
            break

    context = {'rq': record}
    
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())