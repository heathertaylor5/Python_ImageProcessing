from Question1 import addBorders
from Question2 import addDividers
from Question3 import createImageFromBinary
from Question4 import saveImageAsBinary
from Question5 import unscramble4
from Question6 import unscramble9
import sys


def main():
    if len(sys.argv) < 4:
        print("Usage: python a3runner.py function [requirements for function]")
    else:
        args = sys.argv
        toRun = args[1]

        # imageFileName, thickness, colour, outputFileName
        if toRun == "addBorders":
            if len(sys.argv) != 8:
                print(
                    "Usage: python a3runner.py addBorders imageFileName thickness red green blue outputFileName")
            else:
                fileName = args[2]
                thickness = int(args[3])
                colour = (int(args[4]), int(args[5]), int(args[6]))
                outputFileName = args[7]
                addBorders(fileName, thickness, colour, outputFileName)

        # imageFileName, rows, cols, thickness, colour, outputFileName
        elif toRun == "addDividers":
            if len(sys.argv) != 10:
                print(
                    "Usage: python a3runner.py addDividers imageFileName rows cols thickness red green blue outputFileName")
            else:
                fileName = args[2]
                rows = int(args[3])
                cols = int(args[4])
                thickness = int(args[5])
                colour = (int(args[6]), int(args[7]), int(args[8]))
                outputFileName = args[9]
                addDividers(fileName, rows, cols, thickness,
                            colour, outputFileName)

        elif toRun == "createImageFromBinary":
            if len(sys.argv) != 4:
                print(
                    "Usage: python a3runner.py createImageFromBinary sourceFileName targetFileName")
            else:
                fileName = args[2]
                outputFileName = args[3]
                createImageFromBinary(fileName, outputFileName)

        elif toRun == "saveImageAsBinary":
            if len(sys.argv) != 4:
                print(
                    "Usage: python a3runner.py saveImageAsBinary sourceFileName targetFileName")
            else:
                fileName = args[2]
                outputFileName = args[3]
                saveImageAsBinary(fileName, outputFileName)

        # imageFileName, targetFileName
        elif toRun == "unscramble4":
            if len(sys.argv) != 4:
                print(
                    "Usage: python a3runner.py unscamble4 imageFileName outputFileName")
            else:
                fileName = args[2]
                outputFileName = args[3]
                unscramble4(fileName, outputFileName)

        elif toRun == "unscramble9":
            if len(sys.argv) != 4:
                print(
                    "Usage: python a3runner.py unscamble9 imageFileName outputFileName")
            else:
                fileName = args[2]
                outputFileName = args[3]
                unscramble9(fileName, outputFileName)

        else:
            print("Function not Recognized")
            print(
                "Usage: python a3runner.py function [requirements for function]")


if __name__ == "__main__":
    main()
