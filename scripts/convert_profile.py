from PIL import Image
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / 'images' / 'profil.jpg'
OUTPUT = BASE / 'images' / 'profil-rgb.jpg'

print('Input:', INPUT)
print('Output:', OUTPUT)

if not INPUT.exists():
    print('Input file does not exist')
    raise SystemExit(1)

with Image.open(INPUT) as img:
    print('Original mode:', img.mode)
    rgb = img.convert('RGB')
    rgb.save(OUTPUT, quality=95)
    print('Saved RGB image')
