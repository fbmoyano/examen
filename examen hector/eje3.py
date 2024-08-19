from PIL import Image
import os

print("hola porfavor ingrese ruta de imagen")
image = str(input())
imgopen= Image.open(image)
print("ahora el angulo de rotacion ")
angulo= int(input())
img_rot= imgopen.rotate(angulo)
save_img = img_rot.save ("nombreArchivoOriginalRot.extOriginal.jpeg")