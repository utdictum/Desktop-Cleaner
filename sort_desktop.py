import os 
import shutil


file_mappings = {
    '.jpg': 'Images',
    '.png': 'Images',
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
    file_extension = os.path.splitext(file)[1]