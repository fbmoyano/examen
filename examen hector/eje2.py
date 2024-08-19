from PIL import Image
import os 

print("hola porfavor ingrese ruta de imagen")
image = str(input())
imgopen= Image.open(image)
most= Image._show(imgopen)
print("digme que nuevo nombre quiere para su imagen?")
name = input()
new_image= imgopen.save(f"{name}.jpeg")