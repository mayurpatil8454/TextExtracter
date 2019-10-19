import pytesseract as py
import reportlab.platypus as rs
import reportlab.lib.pagesizes as pages
from PIL import Image
import os


py.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#print("The current working directory is", os.getcwd());
files = [];
path = "D:\Study\Blockchain\Images";
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

#for f in files:
    print(len(files))
    print(os.path.join(files[14]))
# team =Image.open(os.path.join(files[0]))
# print(team)
data="";
# for i in range(0, len(files) - 1):
#     #filename = files[14];
#     text = str(((py.image_to_string(Image.open(os.path.join(files[i]))))))
#     text = text.replace('-\n', '');
#     data = data + text;
# #


doc = rs.SimpleDocTemplate("Blockchain.pdf",pagesize=pages.A4,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

doc1 = rs.SimpleDocTemplate("BlockchainImages.pdf",pagesize=pages.A4,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
Story =[];
for i in range(0, len(files) - 1):
    im = Image(os.path.join(files[i]))
    Story.append(im);
doc1.build(Story);

print("end")
