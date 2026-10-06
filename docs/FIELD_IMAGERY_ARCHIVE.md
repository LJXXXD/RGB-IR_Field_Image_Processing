# RGB/IR historical field imagery archive

This archive contains the nine TIFF files too large for regular Git. It is raw byte splitting: no image conversion or lossy compression is performed.

## Restore

1. Download `manifest.json`, `restore.py`, and every `tiff-XX.part-NNN` asset into one folder. Use the exact filenames. The automatic GitHub source-code ZIP does not include these release assets.
2. Install Python 3 if it is unavailable. The script uses only the Python standard library.
3. From the downloaded folder, run:

```sh
python3 restore.py --output ./restored
```

Original paths are restored under `restored/data/field_image/`. Every part and every reconstructed TIFF must match its recorded byte size and SHA-256 before a file receives its final name. Existing output files are never overwritten. Failed temporary outputs are removed.

To check all parts and original TIFF checksums without writing restored images:

```sh
python3 restore.py --verify-only
```

## Ordering and recovery

For each TIFF, concatenate the parts in the exact order listed in `manifest.json`. The script does this automatically. Do not concatenate different TIFF IDs. Keep the manifest and this script with the parts. A missing, renamed, truncated or corrupt part causes verification to fail.

To restore or verify just one TIFF, download its corresponding parts and run `python3 restore.py --file tiff-01 --output ./restored` (replace the ID with one from the inventory below). Keep the full original manifest unchanged.

## File inventory

| ID | Original TIFF | Bytes | Parts | SHA-256 |
|---|---|---:|---:|---|
| tiff-01 | data/field_image/BRC/BRC_20190814_141033.tif | 4294472176 | 4 | 098305809a46b80e2bf2e6785887c97d8e382cb8670ddde2748718c5e4df8337 |
| tiff-02 | data/field_image/BRC/BRC_20190828_140117.tif | 4272714572 | 4 | b2abbf37b663734c0a47b28fd701e429da948577f7b7b9fc955669e7ad77d82e |
| tiff-03 | data/field_image/BRC/BRC_20190904_121517 12pm.tif | 3317102026 | 4 | 834c21900a8e2e1301d0ddcff22cf13a082bdb37d8916fd3d27c6ee77f3c4776 |
| tiff-04 | data/field_image/BRC/BRC_20191008_145306 East west, 1 of1.tif | 3352921214 | 4 | 8cbaa350ff469d82a9efb2e219d82339ff6cf032a0a61276c606cc1fea7301f8 |
| tiff-05 | data/field_image/C1A/C1A_20190814_132517.tif | 2268636232 | 3 | 4acc8b138127e39968f45c9f0176cb606e570ab0d9404331aa9a19760fc077ad |
| tiff-06 | data/field_image/C1A/C1A_20190828_131301.tif | 3289550436 | 4 | d8b6f13f883792e0bdea6787356f277c91a8164f1bb08c066e1dc77b0c15e028 |
| tiff-07 | data/field_image/C1A/C1A_20190916_120028.tif | 2254555416 | 3 | d65e9d0c99c19adf496deddefaaf04ee4dc259eca15dcf1db0ff273ef2358349 |
| tiff-08 | data/field_image/RB/RB_20190814_151550.tif | 3114062260 | 3 | 15d7378b30ad9926083bae57e343d795f86c8b8b31d9edd1bd40d284d744110a |
| tiff-09 | data/field_image/RB/RB_20190824_121031_12pm.tif | 2704979020 | 3 | 5683e826b1c0260b96debbfdc02e725ce5795e0f0d70db6fd8c49a5496dcef55 |

Total original TIFF bytes: 28868993352

Related code commit: `d9cc2d54c982ff6c05332e30473a9c2a6f0fcfda`.

## Restore the complete project

The code and smaller data files are in Git; the nine oversized TIFFs are Release assets. Both are needed for the complete archived project. First download all Release assets into a folder named `rgb-ir-assets`. Run the following commands from its parent directory.

```sh
git clone https://github.com/LJXXXD/RGB-IR_Field_Image_Processing.git
cd RGB-IR_Field_Image_Processing
git checkout d9cc2d54c982ff6c05332e30473a9c2a6f0fcfda
python3 ../rgb-ir-assets/restore.py --output .
```

The script finds `manifest.json` and the parts in the sibling `rgb-ir-assets` directory. The archived `data/field_image/` layout is restored directly inside the cloned project. The full code snapshot is pinned above; later repository commits do not change these archived TIFFs.

## Space and integrity

All parts together require 28,868,993,352 bytes. Restoring all nine TIFFs while retaining the downloaded parts requires another 28,868,993,352 bytes (approximately 58 GB total, plus the code checkout and filesystem overhead). Single-file restoration requires only that TIFF's parts and its output space.

SHA-256 is checked for every part and for the exact reconstructed original TIFF. Keep `manifest.json`, `restore.py` and `RESTORE.md`; the automatic source-code ZIP is not a substitute for the numbered Release assets. A failed restore removes its incomplete `.restoring` file and does not produce a final TIFF. ZIP extraction and image conversion are not needed.
