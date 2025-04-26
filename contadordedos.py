import cv2
import mediapipe as mp
import serial
import time

# Configurar Arduino (ajusta el puerto COM según tu computadora)
arduino = serial.Serial('COM8', 9600)  # Cambia COM3 al puerto de tu Arduino
time.sleep(2)  # Tiempo para que el puerto serial se estabilice

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Definición de los ids de los dedos
dedos_ids = [4, 8, 12, 16, 20]  # Pulgar, índice, medio, anular, meñique

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    dedos_arriba = 0
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))
            
            if lm_list:
                # Pulgar
                if lm_list[dedos_ids[0]][0] > lm_list[dedos_ids[0] - 1][0]:
                    dedos_arriba += 1
                # Otros 4 dedos
                for id in range(1, 5):
                    if lm_list[dedos_ids[id]][1] < lm_list[dedos_ids[id] - 2][1]:
                        dedos_arriba += 1

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Mostrar número en pantalla
    cv2.putText(frame, f'Dedos: {dedos_arriba}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                2, (255, 0, 0), 3)
    
    # Enviar número al Arduino
    arduino.write(str(dedos_arriba).encode())
    time.sleep(0.1)  # Pequeño retardo para no saturar el serial

    cv2.imshow('Detector de Dedos', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Presionar ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
