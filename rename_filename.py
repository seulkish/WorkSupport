import os

folder = "./folder_renamefile"  # 현재 디렉토리
for filename in os.listdir(folder):
    if filename.endswith(".pdf") and "_2026" not in filename:
        name_only = filename.split(".pdf")[0]  # .pdf 제거
        new_name = f"{name_only}_2026.pdf"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))