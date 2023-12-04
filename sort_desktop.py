import os 
import shutil


file_mappings = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
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
    '.prproj': 'PremierePro',
    '.aep': 'AfterEffects',
    '.aet': 'AfterEffects',
    '.lrtemplate': 'Lightroom',
    '.lrcat': 'Lightroom',
    '.pdf': 'Acrobat',
    '.cdr': 'CorelDRAW',
    '.cdt': 'CorelDRAW',
    '.cpt': 'CorelPhotoPaint',
    '.rif': 'CorelPainter',
    '.pat': 'CorelPainter',
}

#os.path.expanduser('~') ind the home directory of the current user, ~ being shorthand for home directory
#os.path.join joins home directory with desktop so its independent from windows 
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')