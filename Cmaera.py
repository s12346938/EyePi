import cv2
from pygst import *


# Define camera parameters
cap = cv2.VideoCapture(0) # 0 for primary camera
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define RTSP pipeline
pipeline = gst.parse_launch(f"v4l2src device=/dev/video0 ! videoconvert ! x264enc ! rtph264pay name=pay ! appsink")

# Start pipeline
pipeline.set_state(gst.STATE_PLAYING)

while True:
    # Capture frame
    ret, frame = cap.read()

    # Process frame (optional)
    # ...

    # Convert frame to GStreamer buffer
    buffer = gst.Buffer.new_wrapped(frame.tobytes())

    # Push buffer into pipeline
    pay = pipeline.get_by_name("pay")
    pay.push(buffer)

    # Check for user input (optional)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Stop pipeline and release resources
pipeline.set_state(gst.STATE_NULL)

cap.release()
