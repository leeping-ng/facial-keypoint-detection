import cv2
import matplotlib.pyplot as plt

def detect_face(path_xml, image, fig_width, scale_factor=1.2, show=True):
    """
    Returns the vertices of each face (x, y, w, h) in a list of lists
    """

    # Load in a haar cascade classifier for detecting frontal faces
    face_cascade = cv2.CascadeClassifier(path_xml)

    # Get list of (x, y, w, h) for each face, where (x, y) are the top left corner
    face_vertices = face_cascade.detectMultiScale(image, scale_factor, 2)

    # make a copy of the original image to plot detections on
    image_with_detections = image.copy()

    if show:
        for (x,y,w,h) in face_vertices:
            # draw a rectangle around each detected face
            cv2.rectangle(image_with_detections,(x,y),(x+w,y+h),(255,0,0),3)
        
        fig = plt.figure(figsize=(fig_width, fig_width/1.5))
        plt.imshow(image_with_detections)
        plt.axis("off")
        plt.show()

    return face_vertices
