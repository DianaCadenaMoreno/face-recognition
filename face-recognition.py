import face_recognition

# Cargar la imagen
image = face_recognition.load_image_file("group_photo.jpg")

# Detectar los rostros
face_locations = face_recognition.face_locations(image)
print("Se encontraron {} rostros en la imagen.".format(len(face_locations)))

# Mostrar ubicaciones de cada rostro
for i, face_location in enumerate(face_locations):
    top, right, bottom, left = face_location
    print(f"Rostro {i+1}: Coordenadas - Superior: {top}, Derecha: {right}, Inferior: {bottom}, Izquierda: {left}")
