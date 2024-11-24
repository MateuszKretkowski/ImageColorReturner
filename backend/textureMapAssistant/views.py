from django.http import JsonResponse
from PIL import Image

def get_items(request):
    return JsonResponse({"items": ["item1", "item2", "item3"]})

def home(request):
    return JsonResponse({"message": "Welcome to the homepage!"})


# outputPath should be something like: "./TestImages/{object}_basicArmor_"
def GetTextureBits(texturePath, objectsList, width, height, outputPath, mapWidth, mapHeight):
    imageList = {}
    texture = Image.open(texturePath)
    listIndex = 0
    for u in range(mapWidth):
        for i in range(mapHeight):
            image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
            imagePixels = image.load()
            x_offset = width * u
            y_offset = height * i
            for x in range(width):
                for y in range(height):
                    color = texture.getpixel((x + x_offset, y + y_offset))
                    imagePixels[x, y] = color
                    r, g, b, a = color
                    alpha = a
                    if alpha > 0:
                        print(color, " : ", imagePixels)
            imageList[objectsList[listIndex]] = image
            listIndex += 1

    return JsonResponse(imageList)
