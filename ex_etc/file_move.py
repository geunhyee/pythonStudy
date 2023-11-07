# excel 파일을 읽어와서
# 특정 위치에 있는 파일을 엑셀에 있는 경로로 이동시키기

# dev : 아무것도 없는 폴더
# back_dev : 이동할 파일들이있는 폴더
    # test.txt , test2.txt
# 경로 정보가 있는 path_file.xlsx

# 엑셀파일을 읽어와서 적혀있는 경로로 이


import os
import pandas as pd
import shutil

# 원본 폴더 경로
def_folder = "./dev_back"
# 경로를 읽어올 파일
excel_file = "path_file.xlsx"

# 경로 읽어오기
df = pd.read_excel(excel_file)
for dir_path in df["path"]:
    filename = os.path.basename(dir_path)
    source_path = os.path.join(dev_folder, filename)
    #복사 하고자 하는 파일 체크
if not os.path.exists(source_path):
    print("경로에 파일없음")
    continue

folder = os.path.dirname(dir_path)
print(folder)
#해당 경로에 폴더가 없으면 생성
if not os.path.exists(folder):
    os.makedirs(folder)
shutil.move(dir_path, dir_path) #파일이동