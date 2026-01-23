import os
from pathlib import Path

# 获取当前脚本所在目录
BASE_DIR = Path(__file__).parent.absolute()

IMG_PATH = os.path.join(BASE_DIR, 'imgs')

def get_img_path(img_name: str, suffix: str = '.png'):
    return os.path.join(IMG_PATH, f"{img_name}{suffix}")