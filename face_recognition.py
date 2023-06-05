import argparse 
import face_recognition

parser = argparse.ArgumentParser()

#인자 등록
parser.add_argument("-i1", "--pic1", required=True)
parser.add_argument("-i2", "--pic2", required=True)

args = parser.parse_args()
print(f"Picture 1 : {args.pic1}")
print(f"Picture 1 : {args.pic2}")

picture_of_me = face_recognition.load_image_file(args.pic1)
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding은 이제 어느 얼굴과도 비교할 수 있는 내가 가진 얼굴 특징의 보편적인 인코딩을 포함하게 되었습니다. 

unknown_picture = face_recognition.load_image_file(args.pic2)
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# 이제 `compare_faces`를 통해 두 얼굴이 같은 얼굴인지 비교할 수 있습니다!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")