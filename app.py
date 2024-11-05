import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import face_recognition
import numpy as np

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Detección de Rostros")

        # Frame izquierdo para cargar la imagen
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.label = tk.Label(self.left_frame, text="Cargar Imagen")
        self.label.pack()

        self.image_label = tk.Label(self.left_frame)
        self.image_label.pack()

        self.load_button = tk.Button(self.left_frame, text="Cargar Imagen", command=self.load_image)
        self.load_button.pack(pady=10)

        # Frame derecho para mostrar resultados
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.result_label = tk.Label(self.right_frame, text="Resultados")
        self.result_label.pack()

        self.result_text = tk.Text(self.right_frame, width=40, height=20)
        self.result_text.pack()

        self.marked_image_label = tk.Label(self.right_frame)
        self.marked_image_label.pack()

    def load_image(self):
        # Aceptar varios tipos de imágenes
        file_path = filedialog.askopenfilename(filetypes=[
            ("All Files", "*.*"),
        ])
        if file_path:
            self.display_image(file_path)
            self.detect_faces(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((300, 300))  # Redimensionar para mostrar en la GUI
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo  # mantener una referencia

    def detect_faces(self, file_path):
        image = face_recognition.load_image_file(file_path)
        face_locations = face_recognition.face_locations(image)

        # Preparar texto de resultados
        self.result_text.delete(1.0, tk.END)  # Limpiar texto previo
        for i, face_location in enumerate(face_locations):
            top, right, bottom, left = face_location
            self.result_text.insert(tk.END, f"Rostro {i + 1}: Coordenadas - Superior: {top}, Derecha: {right}, Inferior: {bottom}, Izquierda: {left}\n")

        # Crear una imagen con los rostros marcados
        image_with_boxes = self.mark_faces(image, face_locations)
        self.show_marked_image(image_with_boxes)

    def mark_faces(self, image, face_locations):
        image_with_boxes = image.copy()
        for face_location in face_locations:
            top, right, bottom, left = face_location
            self.draw_rectangle(image_with_boxes, top, right, bottom, left)
        return image_with_boxes

    def draw_rectangle(self, image, top, right, bottom, left):
        border_thickness = 2

        # Dibujar bordes en el recuadro de la cara
        for y in range(top, bottom):
            for x in range(left, left + border_thickness):  # Izquierda
                image[y, x] = [255, 0, 0]  # Rojo
            for x in range(right - border_thickness, right):  # Derecha
                image[y, x] = [255, 0, 0]  # Rojo
        for x in range(left, right):
            for y in range(top, top + border_thickness):  # Superior
                image[y, x] = [255, 0, 0]  # Rojo
            for y in range(bottom - border_thickness, bottom):  # Inferior
                image[y, x] = [255, 0, 0]  # Rojo

    def show_marked_image(self, image):
        # Convertir a un formato que tkinter puede mostrar
        image = Image.fromarray(image)
        image = image.resize((300, 300))
        self.photo = ImageTk.PhotoImage(image)
        self.marked_image_label.config(image=self.photo)
        self.marked_image_label.image = self.photo  # mantener una referencia

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
