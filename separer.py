import os
import random
import shutil
from pathlib import Path

# Dossier courant
source = Path.cwd()

# Créer dossiers destination
test_img = source.parent / 'images' / 'val'
test_txt = source.parent / 'labels' / 'val'
test_img.mkdir(parents=True, exist_ok=True)
test_txt.mkdir(parents=True, exist_ok=True)

# Récupérer tous les .jpg
images = list(source.glob("*.jpg"))

# Sélectionner 20% aléatoirement
random.seed(42)
selected = random.sample(images, max(1, int(len(images) * 0.2)))

# DÉPLACER (couper/coller)
for img in selected:
    shutil.move(str(img), str(test_img / img.name))
    txt_file = source / f"{img.stem}.txt"
    if txt_file.exists():
        shutil.move(str(txt_file), str(test_txt / txt_file.name))

print(f"✅ {len(selected)} images déplacées vers {test_img}")
