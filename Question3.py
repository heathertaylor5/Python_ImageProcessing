import FileUtils
from PIL import Image, ImageDraw

def createImageFromBinary(sourceFileName, targetFileName):
    #get the file & data from the file
    filePath = "sources/" + sourceFileName
    data = FileUtils.readIntoList(filePath)
    imageString = data[0]
    binvalues = []

    #break the string from the file into an array of 32-bit strings
    for i in range(0, len(imageString), 32):
        temp = imageString[i:i + 32]
        binvalues.append(temp)

    #the width & height are the first 2 values in the array
    imgWidth = int(binvalues[0], 2)
    imgHeight = int(binvalues[1], 2)
    intvalues = []

    #loop through the rest of the values to get the alpha rgb digits
    for i in range(2, len(binvalues)):
        alpha = int(binvalues[i][0:8], 2)        
        red = int(binvalues[i][8:16], 2)
        green = int(binvalues[i][16:24], 2)
        blue = int(binvalues[i][24:32], 2)
        temp = [red, green, blue, alpha]
        intvalues.append(temp)

    #build the new image
    newImg = Image.new("RGBA", (imgWidth, imgHeight), "white")
    for y in range(imgHeight):
        for x in range(imgWidth):
            pixelIndex = y * imgWidth + x
            colour = tuple(intvalues[pixelIndex])
            newImg.putpixel((x,y), colour)
    
    #show and save the new image
    newImg.show(newImg)
    filePath = "outputs/" + targetFileName
    newImg.save(filePath)

def main():
    createImageFromBinary("pixels_small.txt", "testRoad.png")

if __name__ == "__main__":
    import sys
    main()