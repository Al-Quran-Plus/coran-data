# -*- coding: utf-8 -*-
import json
import xml.etree.ElementTree as ET

# Fichiers d'entr�e
with open("../raw_data/vo.json", "r", encoding="utf-8") as f_vo, open("../raw_data/fr.json", "r", encoding="utf-8") as f_fr, open("../raw_data/transliteration.json", "r", encoding="utf-8") as tr:
    vo_data = json.load(f_vo)
    fr_data = json.load(f_fr)
    tr_data = json.load(tr)
    
# Fichier des m�tadonn�es XML
tree = ET.parse("../raw_data/quran-data.xml")
root = tree.getroot()

# R�cup�ration des m�tadonn�es
metadata = {}
for sura in root.findall(".//sura"):
    index = int(sura.attrib["index"])
    metadata[index] = {
        "index": index,
        "name_ar": sura.attrib["name"],
        "name": sura.attrib["ename"],
        "name_trans": sura.attrib["tname"],
        "type": sura.attrib["type"],
        "order": int(sura.attrib["order"]),
        "ayah_count": int(sura.attrib["ayas"])
    }

# Construction vo.json
vo_output = []
for sura in vo_data["quran"]["sura"]:
    idx = int(sura["_index"])
    meta = metadata[idx]
    ayahs = [{"index": int(aya["_index"]), "text": aya["_text"]} for aya in sura["aya"]]
    vo_output.append({**meta, "ayahs": ayahs})

# Construction fr.json
fr_output = []
for sura in fr_data["quran"]["sura"]:
    idx = int(sura["_index"])
    meta = metadata[idx]
    ayahs = [{"index": int(aya["_index"]), "text": aya["_text"]} for aya in sura["aya"]]
    fr_output.append({**meta, "ayahs": ayahs})
    
tr_output = []
for chapter_str, verses_list in tr_data.items():
    idx = int(chapter_str)
    meta = metadata[idx]
    ayahs = [{"index": int(aya["verse"]), "text": aya["text"]} for aya in verses_list]
    tr_output.append({**meta, "ayahs": ayahs})

# Sauvegarde
with open("../pre_processed_data/vo.json", "w", encoding="utf-8") as f_vo_out:
    json.dump(vo_output, f_vo_out, ensure_ascii=False, indent=2)

with open("../pre_processed_data/fr.json", "w", encoding="utf-8") as f_fr_out:
    json.dump(fr_output, f_fr_out, ensure_ascii=False, indent=2)

with open("../pre_processed_data/tr.json", "w", encoding="utf-8") as tr_out:
    json.dump(tr_output, tr_out, ensure_ascii=False, indent=2)