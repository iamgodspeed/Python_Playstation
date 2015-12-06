# a reading frame is a way of dividing the DNA sequence of nucleotides into
# a set of consecutive, non-overlapping triplets (or codons).

# AGGTGACACCGCAAGCCTTATATTAGC

# reading frame 1 : AGG TGA CAC CGC AAG CCT TAT ATT AGC
# reading frame 2 : A GGT GAC ACC GCA AGC CTT ATA TTA GC
# reading frame 3 : AG GTG ACA CCG CAA GCC TTA TAT TAG C

# Open Reading Frame :
# An open reading frame (ORF) is the part of a reading frame that has the potential to encode a protein.
# It starts with a start codon (ATG), and ends with a stop codon (TAA, TAG or TGA).
# For instance, ATG AAA TAG is an ORF of length 9.

# identify all ORFs present in each sequence of the FASTA file
# longest ORF and id
# longest ORF within id

import regex as re

try:
    f = open('/Users/chuan/Desktop/DATA_JHU/1_python_introduction/dna1.fasta')
except IOError:
    print "does not exist"

# seq id + sequence
seqs = {}
for line in f:
    line = line.rstrip()
    if line[0] == '>':
        name = line
        seqs[name] = ''
    else:
        seqs[name] += line
f.close()

print 'all sequences: ', seqs
print 'total many records: ', len(seqs)  #20

'''======================================================='''

# seq id + length
seqs_length = {}
for i in range(len(seqs)):
    name = seqs.keys()[i]
    seqs_length[name] = len(seqs.values()[i])

print "longest record: ",  max(seqs_length.values())   # 4510
print "shortest record: ",  min(seqs_length.values())  # 475

'''======================================================='''

# Open Reading Frame
seq = seqs.values()[1]
# get RF1:
rfs1 = re.findall('...', seq)
print 'rf1: ',rfs1
# get RF2:
rfs2 = re.findall('...', seq[1:])
print 'rf2: ',rfs2
# get RF3:
rfs3 = re.findall('...', seq[2:])
print 'rf3: ',rfs3


rfs = rfs2

# all start codon position
# [20, 42, 93, 131, 282, 288, 346, 1005]
find = 'ATG'
start = [i for i,v in enumerate(rfs) if v == find]
print "start: ", start

# all end codon position
# [8, 12, 62, 97, 153, 171, 328, 381, 394, 401, 407, 541, 563, 581, 595, 607, 616, 692, 702, 712, 744]
find = ['TAA', 'TAG', 'TGA']
end = [i for i,v in enumerate(rfs) if v in find]
print "end: ", end


# get dict {start:end, start:end, ...}
all_orf = {}
used_start = []

for j in range(len(end)):

    for i in range(len(start)):
        if end[j] > start[-i-1] & start[-i-1] not in used_start:
            all_orf[start[-i-1]] = end[j]
            used_start.extend(start[0:-i-1+1])
            break


v = list(map(lambda x: x[0]-x[1], zip(all_orf.values(), all_orf.keys())))

print 'ORF lengths: ', v

idx = v.index(max(v))

print 'longest ORF start idx: ', all_orf.keys()[idx]


'''======================================================='''

'''
seq_example = seqs.values()[0]
import re

print max(re.findall(r'ATG(?:(?!TAA|TAG|TGA)...)*(?:TAA|TAG|TGA)',seq_example), key = len)
'''