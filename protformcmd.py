import sys
import proteinformula as pf

def main(infile, outfile, mode='aa1'):
    with open(infile, 'r') as f1, open(outfile, 'w') as f2:
        for line in f1:
            formula = pf.formula_to_string(pf.compute_formula(line, mode))
            print(line.strip(), formula, file=f2, sep=', ')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SyntaxError("Insufficient arguments.")
    else:
        main(*sys.argv[1:])
