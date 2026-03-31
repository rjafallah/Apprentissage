import os

# Si le script est dans le même dossier que vos fichiers
dossier = "."

# Récupérer tous les fichiers .jpg du dossier
fichiers = [f for f in os.listdir(dossier) if f.lower().endswith('.jpg')]
fichiers.sort()  # Trier par ordre alphabétique

print(f"Trouvé {len(fichiers)} images")

for i, ancien_nom in enumerate(fichiers, start=1):
    # Vérifier que le fichier .txt existe
    ancien_txt = ancien_nom.replace('.jpg', '.txt').replace('.JPG', '.txt')
    
    if os.path.exists(os.path.join(dossier, ancien_txt)):
        nouveau_nom = f"Girafe_{i:03d}"
        
        # Renommer l'image
        os.rename(
            os.path.join(dossier, ancien_nom),
            os.path.join(dossier, f"{nouveau_nom}.jpg")
        )
        
        # Renommer le fichier texte
        os.rename(
            os.path.join(dossier, ancien_txt),
            os.path.join(dossier, f"{nouveau_nom}.txt")
        )
        
        print(f"{ancien_nom} -> {nouveau_nom}.jpg")
    else:
        print(f"Attention : {ancien_txt} manquant pour {ancien_nom}")

print("Terminé !")