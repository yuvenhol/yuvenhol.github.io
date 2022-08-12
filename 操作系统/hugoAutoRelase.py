import os
import shutil 
origin_dict = "/Users/yuwenhao/Library/Mobile Documents/iCloud~md~obsidian/Documents/codeLife"

os.chdir(origin_dict)
shutil.copytree()
for root, dirs, files in os.walk(origin_dict):
    for f in files:
        print(os.path.join(root, f))