from PIL import Image
import random

def CountColors(texturePath):
    texture = Image.open(texturePath)
    colors = {
        "rgb": 0,
        }
    for pixelX in range(texture.width):
        for pixelY in range(texture.height):
            color = texture.getpixel((pixelX, pixelY))
            if (len(color) == 4):
                r, g, b, a = color
                alpha = a
            if color in colors and alpha > 0:
                print("There is one, or more duplicate colors: ", color, " at pixel: ", pixelX, " : ", pixelY)
                return
            else:
                colors[color] = (pixelX, pixelY)
    print("There is NONE duplicate pixels")
    return

def ColorTexture(texturePath, width, height, outputPath):
    texture = Image.open(texturePath)
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    imagePixels = image.load()

    newColorsList = []
    for pixelX in range(texture.width):
        for pixelY in range(texture.height):
            color = texture.getpixel((pixelX, pixelY))
            r, g, b, a = color
            alpha = a
            if alpha > 0:
                randomColor = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), 255)
                if randomColor in newColorsList:
                    print("There is a duplicate in the reworked Texture")
                else:
                    imagePixels[pixelX, pixelY] = randomColor
                newColorsList.append(randomColor)
    image.save(outputPath)



def main(): 
    CountColors("./TestImages/Player.map.png")

    # These are my presets for the map coloring. use the same parameters as your {obj}.map.png .
    # If you don't have a map, you can even color the silhouette with one color. this Funcion will cover the rest.
    ColorTexture("./TestImages/Player.map.png", 64, 80, "./TestImages/Player_reworked.map.png")

if __name__ == "__main__":
    main()