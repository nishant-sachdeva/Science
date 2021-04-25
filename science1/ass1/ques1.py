from dict import rna_to_protein  , dna_to_rna
from sys import argv

import re




def rna_portion(dna_string):
    rna_generated = []

    # here we will generate the string for the RNA corresponding to the dna that was entered :
    for a in dna_string:
        rna_generated.append(dna_to_rna[a])
    
    # print(rna_generated)
    
    return ''.join(reversed(rna_generated))




def generate_protein_sequence( rna_seq ):

    final_protein_sequence =  []
    start = 0

    while start  < len(rna_seq):
        rna_seq = rna_seq[start:]
        start = rna_seq.find('aug')
        protein_sequence_for_this_iteration = []

        while start < len(rna_seq):
            codon = rna_seq[start : start + 3]
            try :
                protein = rna_to_protein[codon]
                # if this works then we have the codon , so all is set
            except:
                print ("\n\nThe proteins are not aligned perfectly. Something went wrong with the codon , Lone Codon found is  "+ codon)
                start = start + 2 
                break
                

            if protein == 'STOP\n':
                # then we know that the sequence has ended
                protein_sequence_for_this_iteration.append(protein)
                start = start + 2
                final_protein_sequence.append(''.join(protein_sequence_for_this_iteration))

                break
            else:
                protein_sequence_for_this_iteration.append(protein  + str('-'))
                start = start + 3
        
        start = start + 1

    return final_protein_sequence



filename = argv[1]

print("Reading Dna from dna.txt")

dna_sequence = open(filename , "r").read()

print("\n\nThe dna sequence to be dealt with is \n\n" + dna_sequence )

rna_seq = rna_portion(dna_sequence)

print("\nThe rna generated is :\n\n" + rna_seq) 

protein_sequence = generate_protein_sequence ( rna_seq )

print ( "\n\nThe final list of the peptides generated is as follows : \n")

for a in range(len(protein_sequence)):
    print (str(a+1) + "  :  "  + str(protein_sequence[a]))
