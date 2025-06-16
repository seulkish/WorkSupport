import os

# 폴더 경로 입력
folder_path = './'  # 여기에 폴더 경로를 입력하세요

# 결과 저장할 파일명
output_file = 'file_list.txt'

# 파일명+확장자 리스트
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 파일로 저장
with open(output_file, 'w', encoding='utf-8') as f:
    for name in file_names:
        f.write(name + '\n')

print(f"총 {len(file_names)}개 파일명을 '{output_file}'에 저장했습니다.")
