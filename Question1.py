from PIL import Image, ImageDraw

def addBorders(imageFileName, thickness, colour, outputFileName):
    # open an image file
    fileLocation = "sources/" + imageFileName
    theImage = Image.open(fileLocation)

    # get the width and height
    width, height = theImage.size

    # top border
    for x in range(0, width):
        for y in range(0, thickness):
            theImage.putpixel((x, y), colour)

    # left border
    for x in range(0, thickness):
        for y in range(0, height):
            theImage.putpixel((x,y), colour)

    # right border
    for x in range((width-thickness), width):
        for y in range(0, height):
            theImage.putpixel((x,y), colour)

    # bottom border
    for x in range(0, width):
        for y in range((height-thickness), height):
            theImage.putpixel ((x,y), colour)
    output = "outputs/" + outputFileName
    theImage.show()
    theImage.save(output)

def main():
    addBorders("space.png", 5, (255, 255, 0), "borderedspace.png")

if __name__ == "__main__":
    main()