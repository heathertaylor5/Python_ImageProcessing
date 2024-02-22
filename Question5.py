from PIL import Image, ImageDraw

def unscramble4(imageFileName, targetFileName):
    #get the scrambled image
    filePath = "sources/" + imageFileName
    theImage = Image.open(filePath)
    width, height = theImage.size

    #find the middle values for the image and determine the intended outside border colour
    widthMiddle = width // 2
    heightMiddle = height // 2
    yellowColour = (255, 255, 0)

    #make an empty array for all the quadrants
    allquadrants = []

    #make an array for the first quadrant and fill it with the pixels
    #add the list to the allquadrants list
    q1 = []
    for x in range(widthMiddle):
        for y in range(heightMiddle):
            pixel = theImage.getpixel((x,y))
            q1.append(pixel)
    
    #build the image for the first quadrant
    q1Img = Image.new("RGB", (widthMiddle, heightMiddle), "white")
    for y in range(heightMiddle):
        for x in range(widthMiddle):
            pixelIndex = y * widthMiddle + x
            colour = tuple(q1[pixelIndex])
            q1Img.putpixel((x,y), colour)
    allquadrants.append(q1Img)        

    #repeat for all four quadrants
    q2 = []
    for x in range(widthMiddle, width):
        for y in range(heightMiddle):
            pixel = theImage.getpixel((x,y))
            q2.append(pixel)

    q2Img = Image.new("RGB", (widthMiddle, heightMiddle), "white")
    for y in range(heightMiddle):
        for x in range(widthMiddle):
            pixelIndex = y * widthMiddle + x
            colour = tuple(q2[pixelIndex])
            q2Img.putpixel((x,y), colour)
    allquadrants.append(q2Img)        

    q3 = []
    for x in range(widthMiddle):
        for y in range(heightMiddle, height):
            pixel = theImage.getpixel((x,y))
            q3.append(pixel)

    q3Img = Image.new("RGB", (widthMiddle, heightMiddle), "white")
    for y in range(heightMiddle):
        for x in range(widthMiddle):
            pixelIndex = y * widthMiddle + x
            colour = tuple(q3[pixelIndex])
            q3Img.putpixel((x,y), colour)
    allquadrants.append(q3Img)        
    
    q4 = []
    for x in range(widthMiddle, width):
        for y in range(heightMiddle, height):
            pixel = theImage.getpixel((x,y))
            q4.append(pixel)
    
    q4Img = Image.new("RGB", (widthMiddle, heightMiddle), "white")
    for y in range(heightMiddle):
        for x in range(widthMiddle):
            pixelIndex = y * widthMiddle + x
            colour = tuple(q4[pixelIndex])
            q4Img.putpixel((x,y), colour)
    allquadrants.append(q4Img)        

    #make empty images for the new 4 quadrants
    topLeftQuadrant = Image.new("RGB", (widthMiddle, heightMiddle), "white")
    topRightQuadrant = Image.new("RGB", (widthMiddle, heightMiddle), "white")
    bottomLeftQuadrant = Image.new("RGB", (widthMiddle, heightMiddle), "white")
    bottomRightQuadrant = Image.new("RGB", (widthMiddle, heightMiddle), "white")

    #for each image in allquadrants, find the corner that is NOT yellow
    for i in allquadrants:
        topLeftCorner = i.getpixel((0,0))
        topRightCorner = i.getpixel((widthMiddle - 1, 0))
        bottomLeftCorner = i.getpixel((0, heightMiddle - 1))
        bottomRightCorner = i.getpixel((widthMiddle - 1, heightMiddle - 1))
        
        if topLeftCorner != yellowColour:
            bottomRightQuadrant = i
        elif topRightCorner != yellowColour:
            bottomLeftQuadrant = i
        elif bottomLeftCorner != yellowColour:
            topRightQuadrant = i
        elif bottomRightCorner != yellowColour:
            topLeftQuadrant = i

    #paste all the images to a new image     
    resultImg = Image.new("RGB", (width, height), "white")
    resultImg.paste(topLeftQuadrant, (0,0, widthMiddle, heightMiddle))
    resultImg.paste(topRightQuadrant, (widthMiddle, 0, width, heightMiddle))
    resultImg.paste(bottomLeftQuadrant, (0, heightMiddle, widthMiddle, height))
    resultImg.paste(bottomRightQuadrant, (widthMiddle, heightMiddle, width, height))

    #save the new image as the unscrambled image
    output = "outputs/" + targetFileName
    resultImg.save(output)

def main():
    unscramble4("sources/scrambled4b.png", "unscrambled4.png")

if __name__ == "__main__":
    import sys
    main()