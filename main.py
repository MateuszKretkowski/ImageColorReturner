from PIL import Image

def CountColors(imagePath):
    image = Image.open(imagePath)
    colors = {
        "rgb": 0,
        }
    for pixelX in range(image.width):
        for pixelY in range(image.height):
            color = image.getpixel((pixelX, pixelY))
            if (len(color) == 4):
                r, g, b, a = color
                alpha = a
            if color in colors and alpha > 0:
                print("There is a duplicate color: ", color, " at pixel: ", pixelX, " : ", pixelY)
                return
            else:
                colors[color] = 1
    print("There is NONE duplicate pixels")
    return



def main():
    CountColors("./TestImages/Player.map.png")

if __name__ == "__main__":
    main()