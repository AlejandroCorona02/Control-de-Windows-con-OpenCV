import cv2
import pygame
import numpy as np

# Inicializa Pygame y carga la música
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(C:\Users\ASUS\Music\Contigo-Sabino ft Sharif.mp3)  # Reemplaza "cancion.mp3" con la ubicación de tu archivo de música

# Inicializa la cámara y configura el reconocimiento de gestos con OpenCV
cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier("haarcascade_hand.xml")  # Utiliza un clasificador Haar previamente entrenado

# Inicializa el estado de reproducción de la música
playing = False

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detecta manos en el marco
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Si se detecta una mano, inicia o detiene la reproducción de música con un gesto
        if w * h > 5000:
            if not playing:
                pygame.mixer.music.play()
                playing = True
            else:
                pygame.mixer.music.stop()
                playing = False
    
    cv2.imshow("Gesture Music Control", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
