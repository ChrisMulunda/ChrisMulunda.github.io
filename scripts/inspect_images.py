from pathlib import Path
from PIL import Image, ImageFile
import imghdr
ImageFile.LOAD_TRUNCATED_IMAGES = True

files = [Path('images/profil.jpg'), Path('images/profil-down.jpg')]
for p in files:
    print('---', p)
    if not p.exists():
        print('MISSING')
        continue
    b = p.read_bytes()
    print('Size:', len(b))
    print('First 16 bytes:', b[:16].hex())
    print('imghdr:', imghdr.what(p))
    try:
        with Image.open(p) as im:
            print('PIL format:', im.format, 'mode:', im.mode)
    except Exception as e:
        print('PIL error:', e)
