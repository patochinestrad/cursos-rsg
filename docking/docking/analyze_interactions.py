#!/usr/bin/env python3
import os
import csv
import xml.etree.ElementTree as ET

BASE_DIR = "plip_results"
OUTPUT_CSV = "plip_interactions_summary.csv"
interaction_tags = {
    'hydrophobic_interactions': 'hydrophobic_interaction',
    'hydrogen_bonds': 'hydrogen_bond',
    'salt_bridges': 'salt_bridge',
    'pi_stacking': 'pi_stacking',
    'pi_cation': 'pi_cation',
    # Add more if needed
}

rows = []

for dirname in sorted(os.listdir(BASE_DIR)):
    dpath = os.path.join(BASE_DIR, dirname)
    if not os.path.isdir(dpath):
        continue

    ligand_name = dirname.removesuffix("_complex")

    xml_file = os.path.join(dpath, "report.xml")
    if not os.path.isfile(xml_file):
        print(f"Skipping {dirname} (no report.xml found)")
        continue

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing {xml_file}: {e}")
        continue

    for bs in root.findall(".//bindingsite"):
        for parent_tag, child_tag in interaction_tags.items():
            for interaction in bs.findall(f".//{parent_tag}/{child_tag}"):
                # Extract receptor residue
                restype = interaction.findtext("restype", default="").strip()
                reschain = interaction.findtext("reschain", default="").strip()
                resnr = interaction.findtext("resnr", default="").strip()
                receptor_residue = f"{restype}{resnr}{reschain}"

                rows.append({
                    "ligand": ligand_name,
                    "interaction_type": child_tag,
                    "receptor_residue": receptor_residue
                })

# Write the CSV
with open(OUTPUT_CSV, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["ligand", "interaction_type", "receptor_residue"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Interaction summary written to {OUTPUT_CSV}")

