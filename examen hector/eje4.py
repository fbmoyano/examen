from PIL import Image
import os

print("porfavor proporcionenos el nombre de una imagen")
imgname = input()
if os.path.exists(imgname):
    img = Image.open(f'{imgname}')
    print("ahora digame donde quiere empezar en x?")
    iniciox = int(input())
    print("ahora digame donde quiere empezar en y?")
    inicioy = int(input())
    print("ahora digame donde quiere empezar el corte de lo ancho?")
    recort1 = int(input())
    print("y el de lo alto?")
    recort2 = int(input())
    imgcort = img.crop((iniciox,inicioy, recort1, recort2))
    newimg = imgcort.save("nueva_imagen.jpeg")

else :
    print("error no existe esa imagen")