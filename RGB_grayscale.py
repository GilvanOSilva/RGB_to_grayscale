from PIL import Image

print("carregando imagem RGB.")
imagem_RGB = Image.open("sample.jpg")
print("criando imagem Gray.")
for x in range(imagem_RGB.width):
    for y in range(imagem_RGB.height):
        cor_Pixel = imagem_RGB.getpixel((x,y))
        cinza = (cor_Pixel[0] + cor_Pixel[1] + cor_Pixel[2]) // 3 
        imagem_RGB.putpixel((x,y),(cinza, cinza, cinza))
imagem_Gray = imagem_RGB.save("sample_gray.jpg")

print("criando imagem PB.")
imagem_Gray = Image.open("sample_gray.jpg")
for x in range(imagem_Gray.width):
    for y in range(imagem_Gray.height):
        cor_Pixel = imagem_Gray.getpixel((x,y))
        if cor_Pixel[0] < 128:
            cor_PB = 0
        else:
            cor_PB = 255
        imagem_Gray.putpixel((x,y),(cor_PB, cor_PB, cor_PB))
imagem_PB  = imagem_Gray.save("sample_PB.jpg")

print("fim do programa.")