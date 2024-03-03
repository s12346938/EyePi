import cv2
from pathlib import Path

# Define model path
model_path = Path("yolov5s.pt")  # Replace with your downloaded model path

# Load the model
model = cv2.dnn_DetectionModel(str(model_path), "")

# Capture video from camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Detect objects
    results = model.detect(frame)

    # Draw bounding boxes and labels (modify as needed)
    classes, confidences, boxes = results.pandas().xyxy[0]
    for i in range(len(classes)):
        class_name, confidence, x_min, y_min, x_max, y_max = classes[i], confidences[i], int(boxes[i][0]), int(boxes[i][1]), int(boxes[i][2]), int(boxes[i][3])
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
        label = f"{class_name}: {confidence:.2f}"
        cv2.putText(frame, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture and clean up
cap.release()
cv2.destroyAllWindows()
