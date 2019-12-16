import cv2
import os
import random


fps = int(input("Selectionnez le nombre de fps "))
image_dir = input("Selectionnez votre dossier d'images ")
name_output_video = input("Selectionnez le nom de la vidéo (output) ")

path_image_dir = 'C:/Users/walte/Desktop/Chaotica/' + image_dir

path_video_name_new = path_image_dir + '/video/' + name_output_video + str(random.randint(0,10000)) + '.avi'

if os.path.isfile(path_image_dir + '/video/' + name_output_video + '.avi'):
    print ("Ce nom de fichier existe déjà ! On te crée un nom un peu différent t'inquiète")
    path_video_name = path_video_name_new 
else:
    print ("Le nom de fichier n'existe pas. Tout va bien !")
    path_video_name = path_image_dir + '/video/' + name_output_video + '.avi'
    

print("Le film charge ! C'est long mdr")
image_folder = path_image_dir
video_name = path_video_name

images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg") or img.endswith(".jepg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, fps, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
print("Ton film vient de se créer !")
