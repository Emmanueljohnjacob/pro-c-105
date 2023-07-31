import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frm=cv2.imread(images[0])
h,w,c=frm.shape
size=(w,h)
out=cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
for i in range(count-1,0,-1):
    frm=cv2.imread(images[i])
    cv2.imshow("video",frm)
    out.write(frm)
    if(cv2.waitKey(25)==32):
        break
out.release()