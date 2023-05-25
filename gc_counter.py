from Bio.Seq import Seq

def gc_counter(dna):
    x = dna.count("G") + dna.count("C")
    y = x / len(dna)
    count = y * 100
    print(f'The GC percentage in your sequence is {count}')

dna = Seq(input("Enter the DNA sequence without the identifiers:"))
gc_counter(str(dna))
