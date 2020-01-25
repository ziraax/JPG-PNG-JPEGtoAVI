import cv2
import os
import random
from tkinter import filedialog
from tkinter import *


fps = int(input("Select the fps of your movie : "))
name_output_video = input("Select the name of the desire video : ")
    #We ask the program to find the directory containing image files
print("Select the directory containing the images : ")

root = Tk()
root.withdraw()
path_image_dir = filedialog.askdirectory() + '/'

    #We define the path of the video that will be created
path_video_name_new = path_image_dir + 'Video made by the Python script' + '/' + name_output_video + str(random.randint(0,10000)) + '.avi'
    #We check if that name (in extenso that path) is already taken, if so we randomize the name of output video


if os.path.isdir(path_image_dir + 'Video made by the Python script'): #If the dir for the video already exists
    print("We are saving the video in the already existing directory")
   
    if os.path.isfile(path_image_dir + 'Video made by the Python script' + '/' + name_output_video + '.avi'): #If the name of the video already exists
        print ("The name of your video already exists ! We are renaming your video differently")
        path_video_name = path_video_name_new 
    else:
        print ("The name of your video does'nt exist ! It's fine ! ")
        path_video_name = path_image_dir + 'Video made by the Python script' + '/' + name_output_video + '.avi'
    
else:
    print ("Creating a directory to save the movie")
    path = path_image_dir + 'Video made by the Python script'

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        
    
    if os.path.isfile(path_image_dir + 'Video made by the Python script' + '/' + name_output_video + '.avi'):
        print ("The name of your video already exists ! We are renaming your video differently")
        path_video_name = path_video_name_new 
    else:
        print ("The name of your video does'nt exist ! It's fine ! ")
        path_video_name = path_image_dir + name_output_video + '.avi'
    
    
    
    path_video_name = path_image_dir + 'Video made by the Python script' + '/' +  name_output_video + '.avi'
    
    


print("The movie is loading...")

    #Redefining variables
image_folder = path_image_dir 
video_name = path_video_name


    #Creating the movie process


images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg") or img.endswith(".jepg")] #Creating an array of images ending with .png .jpg .jepg
frame = cv2.imread(os.path.join(image_folder, images[0])) #Reading first frame
height, width, layers = frame.shape #Defining height, width by the size of this first frame

video = cv2.VideoWriter(video_name, 0, fps, (width,height))

    #Writing the video
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()


    #End of the process

        
print("Movie created.")










