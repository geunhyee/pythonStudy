#pip install easyorc
# pip install opencv-python

#안될경우
#pip uninstall opencv-python
#pip uninstall opencv-contrib-python
#pip uninstall opencv-contrib-python-headless
#pip install opencv-python==4.5.4.60

import easyocr
# reader = easyocr.Reader(['ko'])
# results= reader.readtext('ocr2.PNG')
# for result in results:
#     text = result[1]
#     print(text)

# reader = easyocr.Reader(['en'])
# results= reader.readtext('ocr3.JPG')
# for result in results:
#     text = result[1]
#     print(text)

reader = easyocr.Reader(['en','ko'])
results= reader.readtext('./ex-ocr/img/image5.JPEG')
for result in results:
    text = result[1]
    print(text)
