from PIL import Image
import os

print("hola porfavor ingrese ruta de imagen")
image = str(input())

imgopen= Image.open(image)
most= Image._show(imgopen)

print(f"el nombre de la imagen es :{imgopen.filename}, es formato es : {imgopen.format},la resolucion es :{imgopen.size},la cantidad de pixeles son:{imgopen.height*imgopen.width}, y la ruta es {image}")
