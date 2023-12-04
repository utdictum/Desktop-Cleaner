import os 
import shutil


file_mappings = {
    '.jpg': 'ImagesJPG',
    '.png': 'ImagesPNG',
    '.pdf': 'Documents',
    '.txt': 'Documents',
    '.docx': 'Documents',
    '.psd': 'Photoshop',
    '.psb': 'Photoshop',
    '.abr': 'Photoshop',
    '.ai': 'Illustrator',
    '.ait': 'Illustrator',
    '.indd': 'InDesign',
    '.indt': 'InDesign',
    '.aep': 'AfterEffects',
    '.aet': 'AfterEffects',
    '.lrtemplate': 'Lightroom',
    '.lrcat': 'Lightroom',
    '.cdr': 'CorelDRAW',
    '.cdt': 'CorelDRAW',
    '.pdf': 'Acrobat',
    '.cpt': 'CorelPhotoPaint',
    '.rif': 'CorelPainter',
    '.pat': 'CorelPainter',
}

#os.path.expanduser('~') find the home directory of the current user, ~ being shorthand for home directory
#os.path.join joins home directory with desktop so its independent from windows 
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

#os.listdir(desktop_path) list all the file and directories in the constructed desktop directory
#os.path.isfile(os.path.join(desktop_path, f)) checks if file then joins constructed desktop directory to the f if file
files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]


# MOVING FILES
for file in files:
    #extract file extension based on name
    file_extension = os.path.splitext(file)[1]

    if file_extension in file_mappings:
        #if file in extension in mapping retainn folder name that matches files type
        folder_name = file_mappings[file_extension]
        folder_path = os.path.join(desktop_path, folder_name)
        #if folder with name doesnt exista make it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        #construct file to current location and new     
        file_current_location = os.path.join(desktop_path, file)
        file_new_location = os.path.join(folder_path, file)
        #need to initialise new_file_location with file_new_location
        new_file_location = file_new_location
        #function to move form argument mapping current location to new
        ##FIX FOR OVERWRITING ISSUE
        if os.path.exists(file_new_location):
            base, extension = os.path.splitext(file)
            i = 1
            new_file_name = f"{base}_{i}{extension}"
            new_file_location = os.path.join(folder_path, new_file_name)
            while os.path.exists(new_file_location):
                i += 1
                new_file_name = f"{base}_{i}{extension}"
                new_file_location = os.path.join(folder_path, new_file_name)

        shutil.move(file_current_location, file_new_location)