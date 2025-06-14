# Coran Data Processing

Ce dépôt contient les données et scripts pour le traitement et la segmentation des ayahs du Coran, en vue d’une application d’apprentissage.

---

## Structure du dépôt

- `raw_data/`  
  Contient les fichiers JSON bruts du Coran, tels qu'ils sont fournis à l'origine, sans modification.

- `scripts/`  
  Scripts Python pour traiter les données : formatage, nettoyage.

- `pre_processed_data/`  
  Données après première étape de formatage.  
  Contient également une interface web (`index.html`) pour visualiser et segmenter les ayahs longues.

- `processed_data/`  
  Données finales après segmentation des ayahs.

---

## Utilisation

1. **Formatage des données**  
   Exécuter le script `scripts/format_coran.py` pour transformer les fichiers bruts de `raw_data/` en données formatées dans `pre_processed_data/`.

2. **Segmentation des ayahs longues**  
   Pour utiliser l’interface web `pre_processed_data/index.html` (qui charge les données JSON locales), il faut ouvrir un serveur web local.  
   Par exemple, avec Python :  
   ```bash
    cd pre_processed_data
    python -m http.server 8000
   ```

3. **Sauvegarde des données segmentées**  
   Une fois segmentées, les données sont enregistrées dans `processed_data/` pour utilisation finale dans l'application.

