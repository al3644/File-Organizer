#This was built as a simple, personal project to learn a bit more about Python and File Explorer 

import os, shutil 

#Access where the python script is currently 
path = os.path.dirname(__file__)

#Or access via direct path given
#path = r"path here"

#Checks folder from path given 
startingFolder = os.listdir(path)

FolderTypes = ["Image File", "Video File", "MS File"]

#File types for folders
ImageTypes = ["PNG", "JPG"]
VideoTypes = ["MP4", "AVI"]
MicroSoftTypes = ["PDF", "PPTX", "XLSX", "DOCX"]

#Checks to see if folder exists or not
def exists(p):
    return os.path.exists(p)

#Makes folder if haven't already 
def MakeFolders():
    for folder in FolderTypes:
        if not exists(folder):
            os.mkdir(folder)

MakeFolders() 

def getType(f):
    return f.split(".")[-1].upper()

def moveFolder(file, folder):
    return shutil.move(path + "/" + file, path + "/" + folder + "/" + file)

#Moves files into respective file type
def organizeFiles():
    for file in startingFolder:
        if getType(file) in ImageTypes:
            moveFolder(file, "Image File")
        
        if getType(file) in VideoTypes:
            moveFolder(file, "Video File")

        if getType(file) in MicroSoftTypes:
            moveFolder(file, "MS File")

organizeFiles()