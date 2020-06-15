import pytesseract as py
import reportlab.platypus as rs
import reportlab.lib.pagesizes as pages
from PIL import Image
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os
import cv2


py.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#print("The current working directory is", os.getcwd());
files = [];


#Configure Path
path = "D:\Study\Blockchain\Images";
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        img = cv2.imread(os.path.join(r, file))
        if img is not None:
            files.append(os.path.join(r, file))

doc1 = rs.SimpleDocTemplate("BlockchainImages.pdf",pagesize=pages.A4,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)


Story =[];
##Initialization for Table
Paragraph = rs.Paragraph;
styles = getSampleStyleSheet()


style_right = ParagraphStyle(name='right', parent=styles['Normal'], alignment=TA_RIGHT)

for i in range(0, len(files) - 1):
    im = rs.Image(os.path.join(files[i]),7*inch,4*inch)
    text = str(((py.image_to_string(Image.open(os.path.join(files[i]))))))
    text = text.replace('-\n', '');
    Story.append(im) # appending Image
    Story.append(Paragraph(text, styles["Normal"]))  #Extracted Text
doc1.build(Story)

print("end")
