# Protein Formula Calculator

This was submitted as the first project for my Bioinformatics Programming course in the Spring 2019 semester. Given an amino acid sequence, it calculates the chemical formula.

# Files

```dicts.py``` contains dictionaries to translate between DNA sequences, RNA sequences, amino acid sequences, and chemical formulas.

```proteinformula.py``` contains the core functionality of calculating protein chemical formulas.

```protformgui.pyw``` contains a GUI for accessing the functions. If you're having difficulty running the program, try double-clicking on the file from the file explorer.

```protformcmd.py``` allows for processing of files from the command line. The form of commands is ```protformcmd.py inputfile outputfile mode``` where inputfile is the name of the file containing the sequence to be translated, outputfile is the name of the file to save the output to, and mode specifies the format of the input: ```aa1``` for 1-letter amino acid codes, ```aa3``` for 3-letter amino acid codes, ```dna``` for DNA bases, and ```rna``` for RNA bases. The mode parameter is optional and defaults to ```aa1```. Example usage: ```protformcmd.py mydnaseq.txt output.txt dna``` or ```protformcmd.py myprotein.txt output.txt```. Note that the command-line utility will overwrite the output file if it already exists.
