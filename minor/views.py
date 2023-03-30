from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import os
import cv2
import pytesseract as pt
from PIL import Image
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Create your views here.

def index(request):
    context={'a':1}
    return render(request,'index.html',context)

def predicttext(request):
    if request.method == 'POST':
        file_obj = request.FILES['filepath']
        fs = FileSystemStorage()             #it will help to store the image in the System
        filePathName = fs.save(file_obj.name,file_obj)
        filePathName = fs.url(filePathName)
        image_name = file_obj.name
        print(image_name)
        imageName = image_name
        
        # Actual OCR Code
        # img_path = r'C:\Users\Admin\OCR\media'
        # img = cv2.imread(r"C:\Users\Admin\OCR\media\hand2.png")
        # cv2.imshow("IMAGE", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # text = pytesseract.image_to_data(img)

        test_img_path = r'C:\Users\Admin\OCR\media'
        create_path = lambda f : os.path.join(test_img_path, f)
        test_image_files = os.listdir(test_img_path)
        
        def show_image(img_path, size=(224, 224)):
            image = cv2.imread(img_path)
            image = cv2.resize(image, size)

        image = cv2.imread(r"C:\Users\Admin\OCR\media\hand'.png") 
        # cv2.imshow("IMAGE", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        avb_langs = pt.get_languages(config='hin')
        path = create_path(r"C:\Users\Admin\OCR\media\hand'.png")
        image = Image.open(path)
        
        text = pt.image_to_string(image, lang='hin')



        context = {'filePathName': filePathName, 'imageName':imageName,'text': text }
        return render(request,'index.html',context)

    else:
        return render(request, 'error.html')
