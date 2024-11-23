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

def ColorTextureWithShades(texturePath, width, height, outputPath):
    texture = Image.open(texturePath)
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    imagePixels = image.load()

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    currentColorIndex = 0
    colorsList = []

    for pixelX in range(texture.width):
        for pixelY in range(texture.height):
            color = texture.getpixel((pixelX, pixelY))
            _, _, _, alpha = color
            
            if alpha > 0:
                baseColor = colors[currentColorIndex]
                
                randomShade = (
                    baseColor[0] + random.randint(-50, 50),
                    baseColor[1] + random.randint(-50, 50),
                    baseColor[2] + random.randint(-50, 50),
                    255
                )
                randomShade = tuple(max(0, min(255, c)) for c in randomShade)

                while randomShade in colorsList:
                    print("There is a DUPLICATE, re-rolling...")
                    randomShade = (
                        baseColor[0] + random.randint(-50, 50),
                        baseColor[1] + random.randint(-50, 50),
                        baseColor[2] + random.randint(-50, 50),
                        255
                    )
                    randomShade = tuple(max(0, min(255, c)) for c in randomShade)

                if randomShade in colorsList:
                    print("there is STILL a duplicate")
                else:
                    imagePixels[pixelX, pixelY] = randomShade
                    colorsList.append(randomShade)

            if (pixelX % 16 == 15) and (pixelY % 16 == 15):
                currentColorIndex = (currentColorIndex + 1) % len(colors)

    image.save(outputPath)

def main(): 
    # These are my presets for the map coloring. use the same parameters as your {obj}.map.png .
    # If you don't have a map, you can even color the silhouette with one color. this Funcion will cover the rest.
    ColorTextureWithShades("./TestImages/Player.map.png", 64, 80, "./TestImages/Player_reworked.map.png")

if __name__ == "__main__":
    main()