#TIFF IN TECH
import cv2

class Face_Detection_System:
    def __init__(self, xml_File:str):
        self.face_classifier = cv2.CascadeClassifier(xml_File)

    def detect_face(self, img):
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(grey, 1.3, 5)

        try:
            if faces == ():
                return img
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w,y+h), (255, 0, 0), 2)
                return img
        except Exception as err:
            return err

    def start(self):
        cap = cv2.VideoCapture(0)

        try:
            while True:
                res, frame = cap.read()

                frame = self.detect_face(frame)

                cv2.imshow("Video Face Detection by Kingsley", frame)

                if cv2.waitKey(1) & 0xFF == ord("Q"):
                    break

            cap.release()
            cv2.destroyAllWindows()
        except Exception as err:
            return err



