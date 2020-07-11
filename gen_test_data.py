import face_recognition
import sys
from PIL import Image
import glob

with open('output/data.csv','w') as file:
    face_num = 0
    for filename in glob.glob('input/*.jpg'):

        # Load the jpg file into a numpy array
        image = face_recognition.load_image_file(filename)

        # Find all facial features in all the faces in the image
        face_landmarks_list = face_recognition.face_landmarks(image)

        print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

        for face_landmarks in face_landmarks_list:
            face_num += 1
            
            for facial_feature in face_landmarks.keys():
                file.write("{},{}".format(face_num,facial_feature))
            
                ref_x = face_landmarks[facial_feature][0][0]
                ref_y = face_landmarks[facial_feature][0][1]
                for points in face_landmarks[facial_feature]:
                    file.write(",{}:{}".format(ref_x-points[0],ref_y-points[1]))
            
                file.write("\n")
