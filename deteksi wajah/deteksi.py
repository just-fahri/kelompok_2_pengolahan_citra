# face_detection/deteksi.py
import cv2
import os

def ambil_wajah(output_folder='output_images'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    print("Tekan 's' untuk simpan wajah, 'q' untuk keluar.")
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        wajah = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in wajah:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        cv2.imshow("Deteksi Wajah", frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            if wajah != ():
                wajah_file = os.path.join(output_folder, "wajah_terdeteksi.jpg")
                cv2.imwrite(wajah_file, frame)
                break
        elif key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    return os.path.join(output_folder, "wajah_terdeteksi.jpg")