aa3_to_aa1 = {'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D',
              'CYS': 'C', 'GLN': 'Q', 'GLU': 'E', 'GLY': 'G',
              'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
              'MET': 'M', 'PHE': 'F', 'PRO': 'P', 'SER': 'S',
              'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'}

dna_to_aa1 = {'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'CTT': 'L',
              'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'TTA': 'L',
              'TTG': 'L', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V',
              'GTG': 'V', 'TTT': 'F', 'TTC': 'F', 'ATG': 'M',
              'TGT': 'C', 'TGC': 'C', 'GCT': 'A', 'GCC': 'A',
              'GCA': 'A', 'GCG': 'A', 'GGT': 'G', 'GGC': 'G',
              'GGA': 'G', 'GGG': 'G', 'CCT': 'P', 'CCC': 'P',
              'CCA': 'P', 'CCG': 'P', 'ACT': 'T', 'ACC': 'T',
              'ACA': 'T', 'ACG': 'T', 'TCT': 'S', 'TCC': 'S',
              'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',
              'TAT': 'Y', 'TAC': 'Y', 'TGG': 'W', 'CAA': 'Q',
              'CAG': 'Q', 'AAT': 'N', 'AAC': 'N', 'CAT': 'H',
              'CAC': 'H', 'GAA': 'E', 'GAG': 'E', 'GAT': 'D',
              'GAC': 'D', 'AAA': 'K', 'AAG': 'K', 'CGT': 'R',
              'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R',
              'AGG': 'R', 'TAA': '*', 'TAG': '*', 'TGA': '*'}

rna_to_aa1 = {'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'CUU': 'L',
              'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'UUA': 'L',
              'UUG': 'L', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
              'GUG': 'V', 'UUU': 'F', 'UUC': 'F', 'AUG': 'M',
              'UGU': 'C', 'UGC': 'C', 'GCU': 'A', 'GCC': 'A',
              'GCA': 'A', 'GCG': 'A', 'GGU': 'G', 'GGC': 'G',
              'GGA': 'G', 'GGG': 'G', 'CCU': 'P', 'CCC': 'P',
              'CCA': 'P', 'CCG': 'P', 'ACU': 'T', 'ACC': 'T',
              'ACA': 'T', 'ACG': 'T', 'UCU': 'S', 'UCC': 'S',
              'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
              'UAU': 'Y', 'UAC': 'Y', 'UGG': 'W', 'CAA': 'Q',
              'CAG': 'Q', 'AAU': 'N', 'AAC': 'N', 'CAU': 'H',
              'CAC': 'H', 'GAA': 'E', 'GAG': 'E', 'GAU': 'D',
              'GAC': 'D', 'AAA': 'K', 'AAG': 'K', 'CGU': 'R',
              'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R',
              'AGG': 'R', 'UAA': '*', 'UAG': '*', 'UGA': '*'}

aa1_to_formula = {'A': {'C': 3, 'H': 7, 'N': 1, 'O': 2},
                  'R': {'C': 6, 'H': 14, 'N': 4, 'O': 2},
                  'N': {'C': 4, 'H': 8, 'N': 2, 'O': 3},
                  'D': {'C': 4, 'H': 7, 'N': 1, 'O': 4},
                  'C': {'C': 3, 'H': 7, 'N': 1, 'O': 2, 'S': 1},
                  'Q': {'C': 5, 'H': 10, 'N': 2, 'O': 3},
                  'E': {'C': 5, 'H': 9, 'N': 1, 'O': 4},
                  'G': {'C': 2, 'H': 5, 'N': 1, 'O': 2},
                  'H': {'C': 6, 'H': 9, 'N': 3, 'O': 2},
                  'I': {'C': 6, 'H': 13, 'N': 1, 'O': 2},
                  'L': {'C': 6, 'H': 13, 'N': 1, 'O': 2},
                  'K': {'C': 6, 'H': 14, 'N': 2, 'O': 2},
                  'M': {'C': 5, 'H': 11, 'N': 1, 'O': 2, 'S': 1},
                  'F': {'C': 9, 'H': 11, 'N': 1, 'O': 2},
                  'P': {'C': 5, 'H': 9, 'N': 1, 'O': 2},
                  'S': {'C': 3, 'H': 7, 'N': 1, 'O': 3},
                  'T': {'C': 4, 'H': 9, 'N': 1, 'O': 3},
                  'W': {'C': 11, 'H': 12, 'N': 2, 'O': 2},
                  'Y': {'C': 9, 'H': 11, 'N': 1, 'O': 3},
                  'V': {'C': 5, 'H': 11, 'N': 1, 'O': 2}}
