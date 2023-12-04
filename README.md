# Desktop-Cleaner
File Organizer
Introduction
This Python script automatically organizes files on your desktop into specific folders based on their file extensions. It supports a wide range of file types, including images, documents, and various formats used by Adobe and Corel software.

Installation
To run this script, you need Python installed on your computer. No additional libraries are required as it uses standard Python libraries os and shutil.

Steps:
Ensure Python is installed on your system.
Download the script to your preferred directory.
Usage
To use the script, simply run it from your command line or any Python IDE. The script will sort all files on your desktop into predefined folders. If a folder for a specific file type doesn't exist, it will be created automatically.

Supported File Types and Corresponding Folders:
.jpg, .png -> Images (JPG, PNG)
.pdf, .txt, .docx -> Documents
Adobe Photoshop files (.psd, .psb, .abr) -> Photoshop
Adobe Illustrator files (.ai, .ait) -> Illustrator
Adobe InDesign files (.indd, .indt) -> InDesign
Adobe After Effects files (.aep, .aet) -> AfterEffects
Adobe Lightroom files (.lrtemplate, .lrcat) -> Lightroom
CorelDRAW files (.cdr, .cdt) -> CorelDRAW
Adobe Acrobat files (.pdf) -> Acrobat
Corel Photo-Paint files (.cpt) -> CorelPhotoPaint
Corel Painter files (.rif, .pat) -> CorelPainter
Features
File Sorting: Automatically sorts files into folders based on file extension.
Folder Creation: Creates new folders if they don't already exist.
Duplicate Handling: Renames duplicate files instead of overwriting.
Known Issues
The script currently handles files only on the Desktop. Files in subdirectories are not moved.
Duplicate handling appends a number to the file name, which might result in long file names for multiple duplicates.
Future Improvements
Add support for customizable file paths.
Improve duplicate handling with more sophisticated naming conventions.
Include support for more file types and extensions.