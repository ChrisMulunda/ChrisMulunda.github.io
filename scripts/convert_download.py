from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()
from pathlib import Path

INPUT = Path('images/profil-down.jpg')
OUTPUT = Path('images/profil-rgb.jpg')
print('Opening', INPUT)
with Image.open(INPUT) as im:
    print('Format:', im.format, 'Mode:', im.mode)
    im.convert('RGB').save(OUTPUT, quality=95)
    print('Saved', OUTPUT)
