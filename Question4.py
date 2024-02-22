from PIL import Image, ImageDraw
import FileUtils

def saveImageAsBinary(sourceFileName, targetFileName):
    filePath = "sources/" + sourceFileName
    theImage = Image.open(filePath)
    width, height = theImage.size

    binaryWidth =  "{:032b}".format(width)
    binaryHeight = "{:032b}".format(height)

    pixels = []

    for y in range(height):
        for x in range(width):
            pixel = theImage.getpixel((x, y))
            pixels.append(pixel)

    outputString = binaryWidth + binaryHeight
    for i in pixels:
        red = "{:08b}".format(i[0])
        green = "{:08b}".format(i[1])
        blue = "{:08b}".format(i[2])
        alpha = "11111111"
        outputString += alpha + red + green + blue
    
    
    output = [outputString]
    outputFile = "outputs/" + targetFileName
    FileUtils.writeListToFile(output, outputFile)


def main():
    saveImageAsBinary("sources/road.jpg", "txtRoad.txt")

if __name__ == "__main__":
    import sys
    main()