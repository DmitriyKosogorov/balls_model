import cv2
import os
import matplotlib.pyplot as plt

#3x4 

print("balls")
for i in range(1552):
    print(i,'/1551')
    if(not os.path.exists("D:/dataset_smaller_1/balls/"+str(i)+".jpg")):
        path='D:/dataset_smaller/balls/'+str(i)+'.jpg'
        img=cv2.imread(path)
        if(img.shape[0]<img.shape[1]):
            #print(img.shape[0],' ',img.shape[1])
            img=cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
        resized = cv2.resize(img, (150,200), interpolation = cv2.INTER_AREA)
        path1='D:/dataset_smaller_1/balls/'+str(i)+'.jpg'
        cv2.imwrite(path1, resized)
        #img=cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

print("no_balls")
for i in range(1252):
    print(i,'/1252')
    if(not os.path.exists("D:/dataset_smaller_1/no_balls/"+str(i)+".jpg")):
        path='D:/dataset_smaller/no_balls/'+str(i)+'.jpg'
        img=cv2.imread(path)
        if(img.shape[0]<img.shape[1]):
            #print(img.shape[0],' ',img.shape[1])
            img=cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
        resized = cv2.resize(img, (150,200), interpolation = cv2.INTER_AREA)
        path1='D:/dataset_smaller_1/no_balls/'+str(i)+'.jpg'
        cv2.imwrite(path1, resized)

