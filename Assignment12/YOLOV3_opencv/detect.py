import cv2
import numpy as np

# Load YOLOv3 weights and configuration files
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Define the classes to be detected
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load input image
img = cv2.imread("cycle1.jpg")

# Get image dimensions
height, width, channels = img.shape

# Create blob from input image
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

# Set input blob for the neural network
net.setInput(blob)

# Get output layers from the neural network
layer_names = net.getLayerNames()

output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Run inference on the input blob
outs = net.forward(output_layers)

# Initialize lists to store detected object information
class_ids = []
confidences = []
boxes = []

# Loop over all detected objects
for out in outs:
    for detection in out:
        # Get class scores and class ID with maximum score
        scores = detection[5:]
        class_id = np.argmax(scores)
        
        # Get confidence score
        confidence = scores[class_id]
        
        # Filter out weak detections with confidence threshold of 0.5
        if confidence > 0.1:
            # Scale the bounding box coordinates to the image size
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            
            # Calculate bounding box coordinates
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            
            # Append detected object information to the respective lists
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])

# Perform non-maximum suppression to eliminate overlapping boxes
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Draw bounding boxes and class labels on the input image
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(classes), 3))

if len(indexes) > 0:
    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str(round(confidences[i], 2))
        color = colors[class_ids[i]]
        cv2.rectangle(img, (x,y), (x+w,y+h), color, 2)
        cv2.putText(img, label + " " + confidence, (x, y-5), font, 1, color, 2)

cv2.imwrite("out.jpg",img)
#cv2.imshow("Object Detection", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

