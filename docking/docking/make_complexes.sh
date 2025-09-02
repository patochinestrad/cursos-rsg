#!/bin/bash

# Usage: ./make_complexes.sh receptor.pdbqt

receptor="$1"

if [[ -z "$receptor" || ! -f "$receptor" ]]; then
    echo "Usage: $0 receptor.pdbqt"
    exit 1
fi

outdir="complexes"
mkdir -p "$outdir"

for res in screening_results/*.pdbqt; do
    base=$(basename "$res" .pdbqt)

    tmp="$outdir/${base}_complex.pdbqt"
    out="$outdir/${base}_complex.pdb"

    # Build receptor + first model of ligand into a PDBQT
    {
        cat "$receptor"
        awk '/^MODEL 1/{flag=1; next} /^ENDMDL/{flag=0} flag' "$res"
        echo "END"
    } > "$tmp"

    # Convert to PDB using OpenBabel
    obabel -i pdbqt "$tmp" -o pdb -O "$out"

    # Remove the intermediate PDBQT if not needed
    rm -f "$tmp"
done

echo "PDB complexes written to $outdir/"

