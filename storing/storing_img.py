#Face recognition Apllication Using Python
import cv2
import os
import resources


class store():
    def __init__(self):
        pass
        print("Storing Images working")
    def storee(self):
        video = cv2.VideoCapture(0)

        # model path from the resources
        model_path = resources.Var().face_model

        # initialize the Face Cascad Classifier using Pre Trained Model Haarcascade frontal face detection model
        facedetect = cv2.CascadeClassifier(model_path)

        # get user name for storing the users pictures to train and identify the face for the users
        nameID = str(input("Enter Your Name : "))

        # set a path for storing the appliation users pictures several directoris
        path = 'images/'+nameID

        # print(face_model)

        isExist = os.path.exists(path)

        if isExist:
            print("Hii My dear user, This Name Already Taken...")
            nameId = str(input("Enter Your Name : "))
        else:
            os.makedirs(path)
        count = 0
        while True:
            ret,frame= video.read()
            faces = facedetect.detectMultiScale(frame,1.3,5)
            for x,y,w,h in faces:
                count = count+1
                name = './images/'+nameID+'/'+str(count)+'.jpg'
                print("currently saving iamge is :: "+name)
                cv2.imwrite(name,frame[y:y+h,x:x+w])
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 3)
            cv2.imshow("Capturing Window", frame)
            cv2.waitKey(1)
            if count > 50:
                break
        video.release()
        cv2.destroyAllWindows()