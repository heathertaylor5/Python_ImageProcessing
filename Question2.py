from PIL import Image, ImageDraw

def addDividers(imageFileName, rows, cols, thickness, colour, outputFileName):
    # open an image file
    filePath = "sources/" + imageFileName
    theImage = Image.open(filePath)

    # get the width and height
    width, height = theImage.size

    dividerWidth = width //cols
    dividerHeight = height // rows

    drawer = ImageDraw.Draw(theImage)

    for i in range(1, cols):
        x = (i * dividerWidth) - thickness
        drawer.line([(x,0), (x,height)], fill=colour, width=thickness)
    
    for i in range(1, rows):
        y = (i * dividerHeight) - thickness
        drawer.line([(0,y), (width, y)], fill=colour, width=thickness)

    output = "outputs/" + outputFileName
    theImage.save(output)
    theImage.show()


def main():
    addDividers("space.png", 5, 8, 2, (255,255,255), "space44.png")

if __name__ == "__main__":
    import sys
    main()