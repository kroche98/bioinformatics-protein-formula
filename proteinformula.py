from dicts import *

def slices(s, n):
    """Generate slices of s in chunks if size n"""
    for c in range(0, len(s), n):
        yield s[c:c+n]

def compute_formula(seq, mode='aa1'):
    """Process a sequence into a dictionary containing a protein's chemical formula
    The input mode can be 'aa1' (1-letter aa codes), 'aa3' (3-letter aa codes), 'dna', or rna"""
    
    # first, convert the input to 1-letter amino acid codes
    if mode == 'aa1':
        pass # nothing to do
    elif mode == 'aa3':
        seq = convert_aa3_to_aa1(seq.upper())
    elif mode == 'dna':
        seq = convert_dna_to_aa1(seq.upper())
    elif mode == 'rna':
        seq = convert_rna_to_aa1(seq.upper())
    else:
        seq = '' # invalid mode

    # now compute the formula
    return convert_aa1_to_formula(seq.upper())

def convert_aa3_to_aa1(seq):
    """Convert a string of 3-letter amino acid codes to a string of 1-letter codes"""
    return ''.join(aa3_to_aa1.get(aa3, 'X') for aa3 in slices(seq, 3))

def convert_dna_to_aa1(seq):
    """Convert a string of DNA bases to a string of 1-letter amino acid codes"""
    return ''.join(dna_to_aa1.get(codon, 'X') for codon in slices(seq, 3))
    
def convert_rna_to_aa1(seq):
    """Convert a string of RNA bases to a string of 1-letter amino acid codes"""
    return ''.join(rna_to_aa1.get(codon, 'X') for codon in slices(seq, 3))

def convert_aa1_to_formula(seq):
    """Take a string of 1-letter amino acid codes
    and return a dictionary with the protein's chemical formula.
    Translation will stop early if a stop codon or invalid amino acid is reached.
    """
    formula = dict()
    aa_count = 0 # count how many amino acids we translate
    for aa in seq:
        if aa not in aa1_to_formula.keys():
            break
        aa_count += 1
        for element in aa1_to_formula[aa].keys():
            if element not in formula:
                formula[element] = 0
            formula[element] += aa1_to_formula[aa][element]
    
    # account for the water molecules lost in bonds
    if aa_count > 1:
        H2Os = aa_count - 1
        formula['H'] -= 2*H2Os
        formula['O'] -= H2Os
    
    return formula

def formula_to_string(formula):
    """Given a dictionary of a chemical formula, return a string representing it"""
    return ''.join(element + ('' if formula[element]==1 else str(formula[element])) for element in formula.keys())
