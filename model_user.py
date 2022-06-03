from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout, Input,experimental
from tensorflow.keras.utils import plot_model
from skimage.draw import random_shapes
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

model=load_model("model_1")

cv2.namedWindow("Changed", cv2.WINDOW_NORMAL)
camera=cv2.VideoCapture(0)
while camera.isOpened():
    ret,frame=camera.read()
    mas=[]
    frame_for_model=frame.copy()
    frame_for_model=cv2.rotate(frame_for_model,cv2.cv2.ROTATE_90_CLOCKWISE)
    frame_for_model=cv2.resize(frame_for_model, (150,200), interpolation = cv2.INTER_AREA)
    mas.append(frame_for_model)
    mas=np.array(mas)
    prediction=model.predict(mas)
    classer=prediction[0][0]
    if(classer>=0.5):
        bboxes=prediction[1]
        start_point=(int(bboxes[0,0]*150),int(bboxes[0,1]*200))
        end_point=(int(bboxes[0,2]*150),int(bboxes[0,3]*200))
        frame_for_model=cv2.rectangle(frame_for_model, start_point, end_point, (0,0,255),5)
    else:
        print("no balls on the screen")
    frame_for_model=cv2.rotate(frame_for_model.copy(),cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    frame_for_model=frame_for_model[10:-10,10:-10,:]
    
    cv2.imshow("Changed", frame_for_model)
    
    #cv2.imshow("Camera", frame)
    
    
    key=cv2.waitKey(1)
    
    if(key==ord('q')):
        break
    
camera.release()
cv2.destroyAllWindows()
