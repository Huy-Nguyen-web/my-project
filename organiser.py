#Creating a folder with python-------------------------
import os
import shutil

#Create a function to create a folder and location
def createfolder(directory):
#Step 1: if the folder did not exist -> Create a folder
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("There is an error occured")
#Step 2: Start creating a folder with path
createfolder("./Organiser/")
Folder = ["Document", "App", "Media", "Zip"]
for folder in Folder:
    createfolder("./Organiser/" + folder)

#Create Folder in each big folder
Document = ["Word", "Excel", "Powerpoint", "Text", "Pdf"]
Media = ["Image", "Video", "Music"]

for document in Document:
    createfolder("./Organiser/Document/" + document)

for media in Media:
    createfolder("./Organiser/Media/" + media)
#Moving file to the Organiser file---------------------
source = os.listdir(".")

def destination(path,local):
    return "./Organiser/" + path + "/" + local 


#Condition of the file: if file end with sth -> Move to that specific place
if __name__ == "__main__":
    for files in source:

        #Sort the Document Folder------------------------------------
        if files.endswith(".docx") or files.endswith(".doc"):
            shutil.move(files,destination("Document","Word"))
        if files.endswith(".xlsx") or files.endswith(".cvs"):
            shutil.move(files,destination("Document","Excel"))
        if files.endswith(".ppt") or files.endswith(".pptx"):
            shutil.move(files,destination("Document","PowerPoint"))
        if files.endswith(".pdf") or files.endswith(".PDF"):
            shutil.move(files,destination("Document", "Pdf"))
        if files.endswith(".txt"):
            shutil.move(files,destination("Document","Text"))

        #Sort the Media Folder----------------------------------------
        if files.endswith(".png") or files.endswith(".JPG") or files.endswith(".jpeg") or files.endswith(".jpg") or files.endswith(".gif") or files.endswith(".ico"):
            shutil.move(files,destination("Media","Image"))
        if files.endswith(".mov") or files.endswith(".mp4") or files.endswith(".m4p") or files.endswith(".svi") or files.endswith(".m4v") or files.endswith(".amv"):
            shutil.move(files,destination("Media", "Video"))
        if files.endswith(".mp3") or files.endswith(".msv") or files.endswith(".wav") or files.endswith(".wv"):
            shutil.move(files, destination("Media", "Music"))  

        #Sort the Compress File---------------------------------------
        if files.endswith(".zip") or files.endswith(".rar"):
            shutil.move(files,destination("Zip",''))

        #Sort the App Folder------------------------------------------
        if files.endswith(".exe") or files.endswith(".lnk"):
            if not files.endswith("Peep.exe"): #This is because of the fact that I have changed my program name to Peep, and I don't want the program just move automatically into App Folder
                shutil.move(files,destination("App",''))


