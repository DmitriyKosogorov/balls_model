# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:28:04 2022

@author: User
"""


file=open("D:/dataset_smaller_1/balls/_annotations.csv")
file_1=open("D:/dataset_smaller_1/balls/1_annotations.csv","w")
file_1.write("filename,width,height,class,xmin,ymin,xmax,ymax\n")
a=0
for line in file:
    #print(line)
    filename, size_x, size_y, bbox, bbox_0, bbox_1, bbox_2, bbox_3=line.split(',')
    size_y=int(size_y)
    size_x=int(size_x)
    bbox_0=int(bbox_0)
    bbox_1=int(bbox_1)
    bbox_2=int(bbox_2)
    bbox_3=int(bbox_3)
    if(size_y<size_x):
        size_y,size_x=size_x,size_y
        if(a==60):
            print(bbox_2)
        a,b,c,d=bbox_0, bbox_1, bbox_2,bbox_3
        bbox_0,bbox_1=size_x-d,a
        bbox_2,bbox_3=size_x-b,c

        #bbox_0,bbox_1=size_x-bbox_2,size_y-bbox_1
        #bbox_2,bbox_3=size_x-bbox_3,size_y-bbox_0
        

    diff_x=size_x/150.0
    diff_y=size_y/200.0
    bbox_0=int(bbox_0/diff_y)
    bbox_1=int(bbox_1/diff_y)
    bbox_2=int(bbox_2/diff_x)
    bbox_3=int(bbox_3/diff_x)
    size_y=200
    size_x=150
    size_y=str(size_y)
    size_x=str(size_x)
    bbox_0=str(bbox_0)
    bbox_1=str(bbox_1)
    bbox_2=str(bbox_2)
    bbox_3=str(bbox_3)
    string_to_file=(',').join([filename, size_x, size_y, bbox, bbox_0, bbox_1, bbox_2, bbox_3,])
    string_to_file+='\n'
    file_1.write(string_to_file)
    a+=1
    
file_1.close()
file_1=open("D:/dataset_smaller_1/balls/1_annotations.csv","r")
a=0
file_1.readline()
'''
for line in file_1:
    if(line[0]!=str(a)):
        print(a)
        a=int(line[0])+1
    else:
        a+=1
    
'''