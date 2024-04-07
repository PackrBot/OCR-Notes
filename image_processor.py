from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
from pathlib import Path

ocr = PaddleOCR(use_angle_cls=True, lang='en')

#folderList = []

pth = Path()


#for dirc in pth.iterdir():
#    if (dirc.is_dir() and "notes" in dirc.name):
#        folderList.append(dirc)


#for folder in folderList:

pictureList = []
for file in pth.iterdir():
    if(file.is_file):
        #print(file.name)
        try:
            im = Image.open(file.name)
            im.verify()
            pictureList.append(file)
        except IOError:
            pass

ocrResults = []

for file in pictureList:

    ocrResult = ocr.ocr(file.name, cls=True)
    ocrResults.append(ocrResult)
    
#for result in ocrResults:
#    for idx in range(len(result)):
#        for line in result[idx]:
#            print(line[1][0])
    
with open("results.txt",'w') as output:
    for result in ocrResults:
        for idx in range(len(result)):
            output.write("\n")
            for line in result[idx]:
                output.write(line[1][0] + "\n")
            output.write("\n")
