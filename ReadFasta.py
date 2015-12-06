# FASTA
# > id1 description of id1
# ATGTGTGTCCGTTGTGTAA
# > id2 description of id2
# ccccagtggggagtagggc

try:
    f = open('/Users/chuan/Desktop/DATA_JHU/1_python_introduction/dna.example.fasta')
except IOError:
    print("does not exist")

seqs = {}                          # create a dictionary
for line in f:
    line = line.rstrip()           # discard the newline"\n"
    if line[0] == '>':
        words = line.split()

# ['>gi|142022655|gb|EQ086233.1|43', 'marine', 'metagenome',
# 'JCVI_SCAF_1096627390048', 'genomic', 'scaffold,', 'whole', 'genome', 'shotgun', 'sequence']

        #name = words[0][1:]        # get sequence name
        name = "-".join(words)      # get all info
        seqs[name] = ''
    else:
        seqs[name] = seqs[name] + line
f.close()


for name, seq in seqs.items():     # get key value pair
    print(name, seq)


# count how many records ">"
try:
    f = open('/Users/chuan/Desktop/DATA_JHU/1_python_introduction/dna.example.fasta')
except IOError:
    print("does not exist")

i = 0
for line in f:
    line = line.rstrip()
    if line[0] == '>':
        i = i + 1
f.close()
print(i)


# sort all sequences
try:
    f = open('/Users/chuan/Desktop/DATA_JHU/1_python_introduction/dna.example.fasta')
except IOError:
    print("does not exist")

seqs = {}
for line in f:
    line = line.rstrip()
    if line[0] == '>':
        words = line.split()
        name = "--".join(words)
        seqs[name] = 0
    else:
        seqs[name] = seqs[name]+len(line)
f.close()

print(seqs.values())
print(max(seqs.values()))  # longest sequence
print(min(seqs.values()))  # shortest sequence

print seqs.values().index(512)
print seqs.keys()[23]




