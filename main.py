# import cv2
# import numpy as np
# from ultralytics import YOLO
# import cvzone
# import numpy as np

# def RGB(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE:
#         point = [x, y]
#         print(point)

# cv2.namedWindow('RGB')
# cv2.setMouseCallback('RGB', RGB)
# # Load COCO class names
# with open("coco1.txt", "r") as f:
#     class_names = f.read().splitlines()

# # Load the YOLOv8 model
# model = YOLO("best1.pt")  # Use a pre-trained YOLOv8 model


# # Open the video file (use video file or webcam, here using webcam)
# cap = cv2.VideoCapture(0)
# count=0


# while True:
#     # Read a frame from the video
#     ret, frame = cap.read()
#     if not ret:
#         break

# #    count += 1
# #    if count % 2 != 0:
# #        continue

#     frame = cv2.resize(frame, (1020, 500))
    
#     # Run YOLOv8 tracking on the frame, persisting tracks between frames
#     results = model.track(frame, persist=True)

#     # Check if there are any boxes in the results
#     if results[0].boxes is not None and results[0].boxes.id is not None:
#         # Get the boxes (x, y, w, h), class IDs, track IDs, and confidences
#         boxes = results[0].boxes.xyxy.int().cpu().tolist()  # Bounding boxes
#         class_ids = results[0].boxes.cls.int().cpu().tolist()  # Class IDs
#         track_ids = results[0].boxes.id.int().cpu().tolist()  # Track IDs
#         confidences = results[0].boxes.conf.cpu().tolist()  # Confidence score
       
#         for box, class_id, track_id, conf in zip(boxes, class_ids, track_ids, confidences):
#             c = class_names[class_id]
#             x1, y1, x2, y2 = box
#             cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
#             cvzone.putTextRect(frame,f'{track_id}',(x1,y2),1,1)
#             cvzone.putTextRect(frame,f'{c}',(x1,y1),1,1)

#     cv2.imshow("RGB", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#        break

# # Release the video capture object and close the display window
# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np
from ultralytics import YOLO
import cvzone
import winsound  # For alarm sound on Windows

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# Load COCO class names
with open("coco1.txt", "r") as f:
    class_names = f.read().splitlines()

# Load the YOLOv8 model
model = YOLO("best1.pt")  # Use your trained YOLOv8 model

# Open the video feed (webcam or video file)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1020, 500))

    # Run YOLOv8 tracking on the frame
    results = model.track(frame, persist=True)

    # Flag to indicate if a non-person object is detected
    non_person_detected = False

    if results[0].boxes is not None and results[0].boxes.id is not None:
        # Get detection data
        boxes = results[0].boxes.xyxy.int().cpu().tolist()  # Bounding boxes
        class_ids = results[0].boxes.cls.int().cpu().tolist()  # Class IDs
        track_ids = results[0].boxes.id.int().cpu().tolist()  # Track IDs
        confidences = results[0].boxes.conf.cpu().tolist()  # Confidence scores

        for box, class_id, track_id, conf in zip(boxes, class_ids, track_ids, confidences):
            c = class_names[class_id]
            x1, y1, x2, y2 = box

            # Draw bounding boxes and labels
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cvzone.putTextRect(frame, f'{track_id}', (x1, y2), 1, 1)
            cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1)

            # Check if the detected object is not a person
            if c.lower() != "person":  # Adjust based on your class names
                non_person_detected = True

    # Trigger alarm if a non-person object is detected
    if non_person_detected:
        cvzone.putTextRect(frame, "ALARM: Non-Person Detected!", (50, 50), 2, 2, colorR=(0, 0, 255))
        winsound.Beep(1000, 500)  # Alarm sound (frequency: 1000 Hz, duration: 500 ms)

    # Display the frame
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
