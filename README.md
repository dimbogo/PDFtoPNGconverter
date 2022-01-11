# PDFtoPNGconverter
script that convert pdf file into png images of every particular page

How to install
pip install pdf2image

Windows
Windows users will have to build or download poppler for Windows. I recommend @oschwartz10612 version which is the most up-to-date. You will then have to add the bin/ folder to PATH or use poppler_path = r"C:\path\to\poppler-xx\bin" as an argument in convert_from_path.

Mac
Mac users will have to install poppler for Mac.

Linux
Most distros ship with pdftoppm and pdftocairo. If they are not installed, refer to your package manager to install poppler-utils

Platform-independant (Using conda)
Install poppler: conda install -c conda-forge poppler
Install pdf2image: pip install pdf2image

How to Run:
-You have to place the script file into the folder with pdf file(it should be the only file in that folder)
-Simply run the file in the terminal
-Images will save in the same directory
