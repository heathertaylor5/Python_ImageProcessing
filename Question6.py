from PIL import Image, ImageDraw
#global variable for all sections
#make an empty array for all the sections
allsections = []


def rebuildSectionImg(sectionWidth, sectionHeight, section):
    #build the image for the first quadrant
    Img = Image.new("RGB", (sectionWidth, sectionHeight), "white")
    for y in range(sectionHeight):
        for x in range(sectionWidth):
            pixelIndex = y * sectionWidth + x
            colour = tuple(section[pixelIndex])
            Img.putpixel((x,y), colour)
    allsections.append(Img)  


def unscramble9(imageFileName, outputFileName):
    #get the scrambled image
    theImage = Image.open(imageFileName)
    width, height = theImage.size

    #find the size of each of the 9 sections
    sectionWidth = width // 3
    sectionHeight = height // 3
    yellowColour = (255, 255, 0)

    #make an array for the first section and fill it with the pixels
    #add the list to the allsections list
    #repeat for all 9 sections
    s1 = []
    for x in range(sectionWidth):
        for y in range(sectionHeight):
            pixel = theImage.getpixel((x,y))
            s1.append(pixel)       

    s2 = []
    for x in range(sectionWidth, (sectionWidth * 2)):
        for y in range(sectionHeight):
            pixel = theImage.getpixel((x,y))
            s2.append(pixel)
    
    s3 = []
    for x in range((sectionWidth * 2), (sectionWidth * 3)):
        for y in range(sectionHeight):
            pixel = theImage.getpixel((x,y))
            s3.append(pixel)
    
    s4 = []
    for x in range(sectionWidth):
        for y in range(sectionHeight, (sectionHeight * 2)):
            pixel = theImage.getpixel((x,y))
            s4.append(pixel)
    
    s5 = []
    for x in range(sectionWidth, (sectionWidth * 2)):
        for y in range(sectionHeight, (sectionHeight * 2)):
            pixel = theImage.getpixel((x,y))
            s5.append(pixel)

    s6 = []
    for x in range((sectionWidth * 2), (sectionWidth * 3)):
        for y in range(sectionHeight, (sectionHeight * 2)):
            pixel = theImage.getpixel((x,y))
            s6.append(pixel)
    
    s7 = []
    for x in range(sectionWidth):
        for y in range((sectionHeight * 2), (sectionHeight * 3)):
            pixel = theImage.getpixel((x,y))
            s7.append(pixel)
    
    s8 = []
    for x in range(sectionWidth, (sectionWidth * 2)):
        for y in range((sectionHeight * 2), (sectionHeight * 3)):
            pixel = theImage.getpixel((x,y))
            s8.append(pixel)

    s9 = []
    for x in range((sectionWidth * 2), (sectionWidth * 3)):
        for y in range((sectionHeight * 2), (sectionHeight * 3)):
            pixel = theImage.getpixel((x,y))
            s9.append(pixel)

    #rebuild the each section as its own image
    rebuildSectionImg(sectionWidth, sectionHeight, s1)        
    rebuildSectionImg(sectionWidth, sectionHeight, s2)
    rebuildSectionImg(sectionWidth, sectionHeight, s3)
    rebuildSectionImg(sectionWidth, sectionHeight, s4)
    rebuildSectionImg(sectionWidth, sectionHeight, s5)
    rebuildSectionImg(sectionWidth, sectionHeight, s6)
    rebuildSectionImg(sectionWidth, sectionHeight, s7)
    rebuildSectionImg(sectionWidth, sectionHeight, s8)
    rebuildSectionImg(sectionWidth, sectionHeight, s9)

    #build the new empty image to paste the sections onto
    unscrambledImg = Image.new("RGB", (width, height), "white")

    #for each image, find all 4 corners to determine where the image belongs on the unscrambled picture
    for i in allsections:
        topLeftCorner = i.getpixel((0,0))
        topRightCorner = i.getpixel((sectionWidth - 1, 0))
        bottomLeftCorner = i.getpixel((0, sectionHeight - 1))
        bottomRightCorner = i.getpixel((sectionWidth - 1, sectionHeight - 1))

        if(topLeftCorner == yellowColour and topRightCorner == yellowColour 
           and bottomLeftCorner == yellowColour and bottomRightCorner != yellowColour):
            unscrambledImg.paste(i, (0, 0))
        elif(topLeftCorner == yellowColour and topRightCorner == yellowColour
             and bottomLeftCorner != yellowColour and bottomRightCorner != yellowColour):
            unscrambledImg.paste(i, (sectionWidth, 0))
        elif(topLeftCorner == yellowColour and topRightCorner == yellowColour
             and bottomLeftCorner != yellowColour and bottomRightCorner == yellowColour):
            unscrambledImg.paste(i, ((sectionWidth *2), 0))
        elif(topLeftCorner == yellowColour and topRightCorner != yellowColour
             and bottomLeftCorner == yellowColour and bottomRightCorner != yellowColour):
            unscrambledImg.paste(i, (0, sectionHeight))
        elif(topLeftCorner != yellowColour and topRightCorner != yellowColour
             and bottomLeftCorner != yellowColour and bottomRightCorner != yellowColour):
            unscrambledImg.paste(i, (sectionWidth, sectionHeight))
        elif(topLeftCorner != yellowColour and topRightCorner == yellowColour
             and bottomLeftCorner != yellowColour and bottomRightCorner == yellowColour):
            unscrambledImg.paste(i, ((sectionWidth * 2), sectionHeight))
        elif(topLeftCorner == yellowColour and topRightCorner != yellowColour
             and bottomLeftCorner == yellowColour and bottomRightCorner == yellowColour):
            unscrambledImg.paste(i, (0, (sectionHeight * 2)))
        elif(topLeftCorner != yellowColour and topRightCorner != yellowColour
             and bottomLeftCorner == yellowColour and bottomRightCorner == yellowColour):
            unscrambledImg.paste(i, (sectionWidth, (sectionHeight * 2)))
        elif(topLeftCorner != yellowColour and topRightCorner == yellowColour
             and bottomLeftCorner == yellowColour and bottomRightCorner == yellowColour):
            unscrambledImg.paste(i, ((sectionWidth * 2), (sectionHeight * 2)))
    
    unscrambledImg.show()
    output = "outputs/" + outputFileName
    unscrambledImg.save(output)


def main():
    unscramble9("sources/scrambled9b.png", "unscrambled9.png")

if __name__ == "__main__":
    import sys
    main()