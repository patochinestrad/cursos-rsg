#!/usr/bin/env python3

import os
import argparse
import itertools
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from rdkit import Chem, DataStructs
from rdkit.Chem.Scaffolds import MurckoScaffold
from rdkit.Chem import MACCSkeys


def readSMILES(smiles_file):
    mol_dict = {}
    with open(smiles_file, "r") as f:
        for line in f:
            if line.strip():
                smiles, name = line.strip().split()
                mol = Chem.MolFromSmiles(smiles)
                if mol:
                    mol_dict[name] = mol
    return mol_dict


def morganFPDict(mol_dict):
    return {
        key: Chem.AllChem.GetMorganFingerprintAsBitVect(
            mol, 2, useFeatures=True, nBits=1024
        )
        for key, mol in mol_dict.items()
    }


def murckoScaffoldFPDict(mol_dict):
    return {
        key: Chem.AllChem.GetMorganFingerprintAsBitVect(
            MurckoScaffold.GetScaffoldForMol(mol), 2, useFeatures=True, nBits=1024
        )
        for key, mol in mol_dict.items()
    }


def maccsKeysFPDict(mol_dict):
    return {key: MACCSkeys.GenMACCSKeys(mol) for key, mol in mol_dict.items()}


def tanimotoSimilarity(fp_dict):
    keys_sim = []
    keys = list(fp_dict.keys())
    for key1, key2 in itertools.product(keys, repeat=2):
        sim = DataStructs.FingerprintSimilarity(fp_dict[key1], fp_dict[key2])
        keys_sim.append([key1, key2, sim])
    return keys_sim


def plotSimilarityHeatmap(similarity_list, fptype, output_png, annotate=False):
    df = pd.DataFrame(similarity_list)
    df.columns = ["Mol1", "Mol2", "Similarity"]
    df["Mol1"] = pd.Categorical(
        df["Mol1"], categories=sorted(df["Mol1"].unique()), ordered=True
    )
    df["Mol2"] = pd.Categorical(
        df["Mol2"], categories=sorted(df["Mol2"].unique()), ordered=True
    )
    df = df.set_index(["Mol1", "Mol2"])["Similarity"].unstack()

    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        df,
        vmin=0,
        vmax=1,
        cbar_kws={"label": "Tanimoto Similarity Coefficient"},
        annot=annotate,
    )
    ax.set(
        title=f"Tanimoto Similarity ({fptype})", xlabel="Molecule", ylabel="Molecule"
    )
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_png, dpi=300)
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Generate fingerprint similarity heatmaps from SMILES"
    )
    parser.add_argument("smi_file", help="Input .smi file")
    parser.add_argument(
        "--annotate",
        action="store_true",
        help="Add numeric similarity values to heatmap",
    )

    args = parser.parse_args()

    mols = readSMILES(args.smi_file)

    fingerprints = {
        "morgan": morganFPDict(mols),
        "murcko": murckoScaffoldFPDict(mols),
        "maccs": maccsKeysFPDict(mols),
    }

    for fptype, fpdict in fingerprints.items():
        sim = tanimotoSimilarity(fpdict)
        plotSimilarityHeatmap(
            sim, fptype, f"{fptype}_similarity.png", annotate=args.annotate
        )
        print(f"Saved {fptype}_similarity.png")


if __name__ == "__main__":
    main()
