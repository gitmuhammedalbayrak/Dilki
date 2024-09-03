# Dilki

**Dilki** is a Python project designed to analyze Turkish syllables by examining their structures and harmonies. The project includes two main classes, `HeceEk` and `VeriDiz`, which work together to generate syllables, check their harmony, and store the results in a SQLite database. This repository serves as the main file for the project.

## Classes and Functions

### HeceEk Class
The `HeceEk` class contains functions that generate different types of syllables and save them to files:

- `kok_hece_oldur(dosyala=False)`: Generates root syllables and optionally saves them to a file.
- `gizli_kavusuk_heceler_oldur(dosyala=False)`: Generates hidden diphthong syllables and optionally saves them to a file.
- `acik_kavusuk_heceler_oldur(dosyala=False)`: Generates open diphthong syllables and optionally saves them to a file.
- `eksik_heceliler_oldur(dosyala=False)`: Saves incomplete syllables to a file.
- `tek_heceliler_oldur()`: Generates all single-syllable structures.
- `iki_heceli_oldur_kalip(ilk_kategori, ikinci_kategori, ic_liste_numarasi, dosya_adi, kucuk_harfi, dosyala=True, buyuk_harfi="B")`: Generates combinations of two syllables and optionally saves them to a file.
- `iki_heceliler_oldur()`: Generates all two-syllable structures.

### VeriDiz Class
The `VeriDiz` class contains functions that check the vowel and consonant harmony of syllables and write the data to a SQLite database:

- `buukk(kelime)`: Checks major vowel harmony in terms of thickness.
- `buuik(kelime)`: Checks major vowel harmony in terms of thinness.
- `buuk(kelime)`: Checks general major vowel harmony.
- `kuudk(kelime)`: Checks minor vowel harmony in terms of flatness.
- `kuuy1k(kelime)`: Checks minor vowel harmony in terms of roundness (first check).
- `kuuy2k(kelime)`: Checks minor vowel harmony in terms of roundness (second check).
- `u_i_s(kelimeu)`: Checks whether the word can be analyzed for harmony.
- `hla(rakam1, rakam2)`: Returns the name of the syllable list.
- `veri_yaz()`: Writes all data to the SQLite database.

### Gosteri Class
The `Gosteri` class has a function that sequentially runs all the operations above:

- `emir()`: Initiates syllable and data processing and completes the operations.

## Usage

The project can be run to analyze syllable structures and harmonies. The `Gosteri.emir()` function starts all operations and prints the results to the screen.

## Installation

1. Clone the project to your local machine or download it as a ZIP file.
2. Run the `Gosteri.emir()` function in a Python environment.

## License

This project is licensed under the T1 License. Please contact me for license details.
