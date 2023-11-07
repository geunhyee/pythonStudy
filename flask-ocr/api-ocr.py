import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import easyocr
import cv2


reader = easyocr.Reader(['en','ko'])
def fn_get_text(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    height , width = img.shape
    result = reader.readtext(img)
    print(result)
    result_dataset =[]
    for bbox, text, prob in result :
        if prob > 0.1: #텍스트일 것이야라는 확률( 0.1보다 크면 텍스트일것이다.)
            result_dataset.append({'text':text, 'bbox':bbox, 'prob':prob})
    for i, v in enumerate(result_dataset):
        print(v['text'], v['bbox'],v['prob'])

    draw_bbox(path, result_dataset)
        #영역 색깔칠하기
def draw_bbox(path, data):
    img = cv2.imread(path)
    for d in data:
        bbox = d['bbox']
        start_point = tuple(bbox[0]) #왼쪽상단
        end_point = tuple(bbox[2])  #오른쪽 하단
        #사각형 그리기
        color = (0, 255, 0)
        thinkness = 2
        img = cv2.rectangle(img, start_point, end_point, color, thinkness)
    cv2.imwrite('ouput.jpg', img)
if __name__ == '__main__':
    fn_get_text('code2.png')
