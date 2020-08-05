# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

print("\nEntrez votre séquence d'ARN ou d'ADN non transcrit à traduire")
sequence=input().upper()

if 'T' in sequence:
  print("\nNous allons étudier la séquence d'ADN suivante:",sequence)
else:
  print("\nNous allons étudier la séquence d'ARN suivante", sequence)
dicoAA={}
dicoAA['AAA'] = ['Lys']
dicoAA['AAG'] = ['Lys']
dicoAA['AAU'] = ['Asn']
dicoAA['AAT'] = ['Asn']
dicoAA['AAC'] = ['Asn']
dicoAA['AUA'] = ['Ile']
dicoAA['ATA'] = ['Ile']
dicoAA['AUU'] = ['Ile']
dicoAA['ATT'] = ['Ile']
dicoAA['AUC'] = ['Ile']
dicoAA['ATC'] = ['Ile']
dicoAA['AUG'] = ['Met']
dicoAA['ATG'] = ['Met']
dicoAA['ACA'] = ['Thr']
dicoAA['ACU'] = ['Thr']
dicoAA['ACT'] = ['Thr']
dicoAA['ACC'] = ['Thr']
dicoAA['ACG'] = ['Thr']
dicoAA['AGA'] = ['Arg']
dicoAA['AGU'] = ['Ser']
dicoAA['AGT'] = ['Ser']
dicoAA['AGC'] = ['Ser']
dicoAA['AGG'] = ['Arg']
dicoAA['CAA'] = ['Gln']
dicoAA['CAC'] = ['Hist']
dicoAA['CAU'] = ['Hist']
dicoAA['CAT'] = ['Hist']
dicoAA['CAG'] = ['Gln']
dicoAA['CUA'] = ['Leu']
dicoAA['CTA'] = ['Leu']
dicoAA['CUC'] = ['Leu']
dicoAA['CTC'] = ['Leu']
dicoAA['CUU'] = ['Leu']
dicoAA['CTT'] = ['Leu']
dicoAA['CUG'] = ['Leu']
dicoAA['CTG'] = ['Leu']
dicoAA['CCA'] = ['Pro']
dicoAA['CCC'] = ['Pro']
dicoAA['CCU'] = ['Pro']
dicoAA['CCT'] = ['Pro']
dicoAA['CCG'] = ['Pro']
dicoAA['CGA'] = ['Arg']
dicoAA['CGC'] = ['Arg']
dicoAA['CGU'] = ['Arg']
dicoAA['CGT'] = ['Arg']
dicoAA['CGG'] = ['Arg']
dicoAA['GAA'] = ['Glu']
dicoAA['GAC'] = ['Asp']
dicoAA['GAU'] = ['Asp']
dicoAA['GAT'] = ['Asp']
dicoAA['GAG'] = ['Glu']
dicoAA['GCA'] = ['Ala']
dicoAA['GCC'] = ['Ala']
dicoAA['GCU'] = ['Ala']
dicoAA['GCT'] = ['Ala']
dicoAA['GCG'] = ['Ala']
dicoAA['GGA'] = ['Gly']
dicoAA['GGC'] = ['Gly']
dicoAA['GGU'] = ['Gly']
dicoAA['GGT'] = ['Gly']
dicoAA['GGG'] = ['Gly']
dicoAA['GUA'] = ['Val']
dicoAA['GTA'] = ['Val']
dicoAA['GUC'] = ['Val']
dicoAA['GTC'] = ['Val']
dicoAA['GUU'] = ['Val']
dicoAA['GTT'] = ['Val']
dicoAA['GUG'] = ['Val']
dicoAA['GTG'] = ['Val']
dicoAA['UAA'] = ['_']
dicoAA['TAA'] = ['_']
dicoAA['UAC'] = ['Tyr']
dicoAA['TAC'] = ['Tyr']
dicoAA['UAG'] = ['_']
dicoAA['TAG'] = ['_']
dicoAA['UAU'] = ['Tyr']
dicoAA['TAT'] = ['Tyr']
dicoAA['UCA'] = ['Ser']
dicoAA['TCA'] = ['Ser']
dicoAA['UCC'] = ['Ser']
dicoAA['TCC'] = ['Ser']
dicoAA['UCU'] = ['Ser']
dicoAA['TCT'] = ['Ser']
dicoAA['UCG'] = ['Ser']
dicoAA['TCG'] = ['Ser']
dicoAA['UGA'] = ['_']
dicoAA['TGA'] = ['_']
dicoAA['UGC'] = ['Cys']
dicoAA['TGC'] = ['Cys']
dicoAA['UGU'] = ['Cys']
dicoAA['TGT'] = ['Cys']
dicoAA['UGG'] = ['Trp']
dicoAA['TGG'] = ['Trp']
dicoAA['UUA'] = ['Leu']
dicoAA['TTA'] = ['Leu']
dicoAA['UUC'] = ['Phe']
dicoAA['TTC'] = ['Phe']
dicoAA['UUU'] = ['Phe']
dicoAA['TTT'] = ['Phe']
dicoAA['UUG'] = ['Leu']
dicoAA['TTG'] = ['Leu']

x=(len(sequence))
if 'T' in sequence:
  print("\nCette séquence d'ADN contient",x, "nucléotides")
else:
  print("\nCette séquence d'ARN contient",x,"nucléotides")
  
print("\nNous pouvons découper cette séquence en triplet de nucléotides ou codons\n")
print([sequence[i:i+3] for i in range(0, len(sequence),3)])

y=int(x/3)
if 'T' in sequence:
  print("\nCette séquence d'ADN devrait donc coder donc pour",y,"acides aminés sauf si on rencontre un codon STOP en cours de traduction...")
else:
  print ("\nCette séquence d'ARN devrait coder donc pour",y,"acides aminés sauf si on rencontre un codon STOP en cours de traduction...")
print("\nChaque triplet ou codon correspond à un acide aminé selon le code génétique\n")

def extrcod(sequence, numero):
  debut = numero * 3
  return sequence[debut:debut+3]

for n in range(0,len(sequence)):
 triplet = extrcod(sequence,n)
 print(dicoAA[triplet])
 if triplet in ['UAA','UGA','UAG','TAA','TGA','TAG']:
   break

print ("\nVoici donc notre protéine avec sa séquence d'acides aminés")