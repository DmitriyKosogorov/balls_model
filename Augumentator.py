import cv2
import os

file=open("D:/dataset_smaller/balls/_annotations.csv")
file_1=open("D:/dataset_smaller/balls/2_annotations.csv","w")
all_lines=file.readlines()
for i in range(388):
    if(not os.path.exists("D:/dataset_smaller/balls/"+str(388+i)+".jpg")):
        path='D:/dataset_smaller/balls/'+str(i)+'.jpg'
        img=cv2.imread(path)
        img=cv2.flip(img,0)
        cv2.imwrite("D:/dataset_smaller/balls/"+str(388+i)+".jpg",img)
    liner=all_lines[i]
    filename, size_x, size_y, bbox, bbox_0, bbox_1, bbox_2, bbox_3=liner.split(',')
    filename=str(i+388)+".jpg"
    bbox_1, bbox_3=str(int(size_y)-int(bbox_3)),str(int(size_y)-int(bbox_1))
    new_liner=(',').join([filename, size_x, size_y, bbox, bbox_0, bbox_1, bbox_2, bbox_3])+"\n"
    new_liner=new_liner.replace('\n','')
    new_liner=new_liner+'\n'
    file_1.write(new_liner)
    
for i in range(388):
    if(not os.path.exists("D:/dataset_smaller/balls/"+str(388*2+i)+".jpg")):
        path='D:/dataset_smaller/balls/'+str(i)+'.jpg'
        img=cv2.imread(path)
        img=cv2.flip(img,1)
        cv2.imwrite("D:/dataset_smaller/balls/"+str(388*2+i)+".jpg",img)
    liner=all_lines[i]
    filename, size_x, size_y, bbox, bbox_0, bbox_1, bbox_2, bbox_3=liner.split(',')
    filename=str(388*2+i)+".jpg"
    bbox_0, bbox_2=str(int(size_x)-int(bbox_2)),str(int(size_x)-int(bbox_0))
    new_liner=(',').join([filename, size_x, size_y, bbox, bbox_0, bbox_1, bbox_2, bbox_3])
    new_liner=new_liner.replace('\n','')
    new_liner=new_liner+'\n'
    file_1.write(new_liner)
        

for i in range(388):
    if(not os.path.exists("D:/dataset_smaller/balls/"+str(388*3+i)+".jpg")):
        path='D:/dataset_smaller/balls/'+str(i)+'.jpg'
        img=cv2.imread(path)
        img=cv2.flip(img,-1)
        cv2.imwrite("D:/dataset_smaller/balls/"+str(388*3+i)+".jpg",img)
    liner=all_lines[i]
    filename, size_x, size_y, bbox, bbox_0, bbox_1, bbox_2, bbox_3=liner.split(',')
    filename=str(388*3+i)+".jpg"
    bbox_0, bbox_2=str(int(size_x)-int(bbox_2)),str(int(size_x)-int(bbox_0))
    bbox_1, bbox_3=str(int(size_y)-int(bbox_3)),str(int(size_y)-int(bbox_1))
    new_liner=(',').join([filename, size_x, size_y, bbox, bbox_0, bbox_1, bbox_2, bbox_3])+"\n"
    new_liner=new_liner.replace('\n','')
    new_liner=new_liner+'\n'
    file_1.write(new_liner)

for i in range(313):
    if(not os.path.exists("D:/dataset_smaller/no_balls/"+str(313+i)+".jpg")):
        path='D:/dataset_smaller/no_balls/'+str(i)+'.jpg'
        img=cv2.imread(path)
        img=cv2.flip(img,0)
        cv2.imwrite("D:/dataset_smaller/no_balls/"+str(313+i)+".jpg",img)
        print("A")
    if(not os.path.exists("D:/dataset_smaller/no_balls/"+str(313*2+i)+".jpg")):
        path='D:/dataset_smaller/no_balls/'+str(i)+'.jpg'
        img=cv2.imread(path)
        img=cv2.flip(img,1)
        cv2.imwrite("D:/dataset_smaller/no_balls/"+str(313*2+i)+".jpg",img)
        print("B")
    if(not os.path.exists("D:/dataset_smaller/no_balls/"+str(313*3+i)+".jpg")):
        path='D:/dataset_smaller/no_balls/'+str(i)+'.jpg'
        img=cv2.imread(path)
        img=cv2.flip(img,-1)
        cv2.imwrite("D:/dataset_smaller/no_balls/"+str(313*3+i)+".jpg",img)
        print("C")
    
file.close()
file_1.close()
