from PIL import Image

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


def main(): 
    CountColors("./TestImages/Player.map.png")

if __name__ == "__main__":
    main()