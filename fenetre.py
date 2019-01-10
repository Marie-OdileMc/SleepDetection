from tkinter import *
from tkinter import font


from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import pyglet
import argparse
import imutils
import time
import dlib
import cv2


def lancerapp(x):
    


        def eye_aspect_ratio(eye):
	        # compute the euclidean distances between the two sets of
	        # vertical eye landmarks (x, y)-coordinates
	        A = dist.euclidean(eye[1], eye[5])
	        B = dist.euclidean(eye[2], eye[5])

	        # compute the euclidean distance between the horizon
	        # eye landmark (x, y)-coordinates
	        C = dist.euclidean(eye[0], eye[3])

	        # compute the eye aspect ratio
	        ear = (A + B) / (2.0 * C)

	        # return the eye aspect ratio
	        return ear
 
        # construct the argument parse and parse the arguments
        ap = argparse.ArgumentParser()

        ap.add_argument("-w", "--webcam", type=int, default=0,
	        help="index of webcam on system")
        args = vars(ap.parse_args())
 
        # define two constants, one for the eye aspect ratio to indicate
        # blink and then a second constant for the number of consecutive
        # frames the eye must be below the threshold for to set off the
        # alarm
        #Si on est dans un situaion ou il faut etre tres vigilant on peut rendre la deuxieme constante plus petite
        EYE_AR_THRESH = 0.3
        EYE_AR_CONSEC_FRAMES = x

        #EYE_AR_CONSEC_FRAMES = 48

        # initialize the frame counter as well as a boolean used to
        # indicate if the alarm is going off
        COUNTER = 0
      

        # initialize dlib's face detector (HOG-based) and then create
        # the facial landmark predictor
        print("[INFO] loading facial landmark predictor...")
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("68 face landmarks.dat")

        # grab the indexes of the facial landmarks for the left and
        # right eye, respectively
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        # start the video stream thread
        print("[INFO] starting video stream thread...")
        vs = VideoStream(src=args["webcam"]).start()
        time.sleep(1.0)

        # loop over frames from the video stream
        while True:
	        # grab the frame from the threaded video file stream, resize
	        # it, and convert it to grayscale 
	        # channels)
            #On passe en gris pour mieux detecter les contrastes
	        frame = vs.read()
	        frame = imutils.resize(frame, width=700)
	        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	        # detect faces in the grayscale frame
	        rects = detector(gray, 0)

	        # loop over the face detections
	        for rect in rects:
		        # determine the facial landmarks for the face region, then
		        # convert the facial landmark (x, y)-coordinates to a NumPy
		        # array
		        shape = predictor(gray, rect)
		        shape = face_utils.shape_to_np(shape)

		        # extract the left and right eye coordinates, then use the
		        # coordinates to compute the eye aspect ratio for both eyes
		        leftEye = shape[lStart:lEnd]
		        rightEye = shape[rStart:rEnd]
		        leftEAR = eye_aspect_ratio(leftEye)
		        rightEAR = eye_aspect_ratio(rightEye)

		        # average the eye aspect ratio together for both eyes
		        ear = (leftEAR + rightEAR) / 2.0

		        # compute the convex hull for the left and right eye, then
		        # visualize each of the eyes
		        leftEyeHull = cv2.convexHull(leftEye)
		        rightEyeHull = cv2.convexHull(rightEye)
		        cv2.drawContours(frame, [leftEyeHull], -1, (182, 196, 46), 1)
		        cv2.drawContours(frame, [rightEyeHull], -1, (182, 196, 46), 1)

		        # check to see if the eye aspect ratio is below the blink
		        # threshold, and if so, increment the blink frame counter
		        if ear < EYE_AR_THRESH:
			        COUNTER += 1

			        # if the eyes were closed for a sufficient number of
			        # then sound the alarm
			        if COUNTER >= EYE_AR_CONSEC_FRAMES:
				        # if the alarm is not on, turn it on
				       

				        # draw an alarm on the frame
				        cv2.putText(frame, "Signes de somnolence!", (10, 30),
					        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (54, 29, 231), 2)
                        #Lancer une autre application !

		        # otherwise, the eye aspect ratio is not below the blink
		        # threshold, so reset the counter and alarm
		        else:
			        COUNTER = 0
			       

		        # draw the computed eye aspect ratio on the frame to help
		        # with debugging and setting the correct eye aspect ratio
		        # thresholds and frame counters
		        cv2.putText(frame, "Rapport d'ouverture: {:.2f}".format(ear), (400, 30),
			        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 196, 46), 2)
 
	        # show the frame
	        cv2.imshow("Frame", frame)
	        key = cv2.waitKey(1) & 0xFF
 
	        # if the `q` key was pressed, break from the loop
	        if key == ord("q"):
		        break

        # do a bit of cleanup
        cv2.destroyAllWindows()
        vs.stop()


def b1():
    lancerapp(30)

def b2():
    lancerapp(18)

def b3():
    lancerapp(8)

fenetre = Tk()

titlefont = font.Font(fenetre, ("Verdana", 14, "bold"))
fontbase = font.Font(fenetre, ("Verdana", 10))

fenetre.geometry("700x250")

fenetre['bg']='#b3e5fc' 

Label(fenetre, text="Bonjour, quel niveau d'attention est necessaire?", bg = '#b3e5fc', font=titlefont).pack(pady=20)

Button(fenetre, text="Bas", bg = '#e1f5fe', relief=GROOVE, font=fontbase, command=b1).pack(pady=10)
Button(fenetre, text="Normal", bg = '#e1f5fe', relief=GROOVE, font=fontbase, command=b2).pack(pady=5)
Button(fenetre, text="Tres haut", bg = '#e1f5fe', relief=GROOVE, font=fontbase, command=b3).pack(pady=5)

Button(fenetre, text="Fermer", relief=RIDGE, font=fontbase, command=fenetre.quit).pack(side=BOTTOM, pady=5)


fenetre.mainloop()

