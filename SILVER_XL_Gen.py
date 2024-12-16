import os

# Set output file path and name
outputFilePath = "X:\\Cyberpunk 2077\\archive\\pc\\mod\\"
outputFileName = "YourCoolXLFile"

# Define ent file list
entList = [ 
    "path\\to\\some.ent",
    "path\\to\\some_other.ent",
]
# Define anims to append
animList = [ 
    "path\\to\\some.anims",
    "path\\to\\some_other.anims",
]

print(f"\nSILVER-XL-GEN |==============================================================|")
if not os.path.exists(outputFilePath):
    print(f"\033[91mPath '{outputFilePath}' not found. Saving XL file next to the Python script.\033[0m")
    outputFilePath = os.path.dirname(os.path.abspath(__file__)) + os.sep

outputLines = []
outputLines.append("animations:")
for ent in entList:
    outputLines.append(f"\t- entity: {ent}")
    for anim in animList:
        outputLines.append(f"\t\tset: {anim}")

outputFile = os.path.join(outputFilePath, outputFileName + ".archive.xl")
with open(outputFile, "w") as file:
    file.write("\n".join(outputLines))

print(f"\033[92mXL File saved to: {outputFile}\033[0m\n")