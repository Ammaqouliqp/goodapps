import cv2

image1_path = 'path/to/your/image1.jpg'
image2_path = 'path/to/your/image2.jpg'

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

faces1 = detect_faces(image1)
faces2 = detect_faces(image2)

num_faces1 = len(faces1)
num_faces2 = len(faces2)

total_faces = num_faces1 + num_faces2
error_percentage = (abs(num_faces1 - num_faces2) / total_faces) * 100

print(f"number of faces on the picture 1: {num_faces1}")
print(f"number of faces on the picture 2 {num_faces2}")
print(f"change percent: {error_percentage:.2f}%")
