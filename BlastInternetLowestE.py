from Bio.Blast import NCBIWWW

fasta_string = 'TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGA\
TGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGAT\
ATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCT\
TCTCATTCTTCTTTGGCACCTACGGTAGAG'

result_handle = NCBIWWW.qblast("blastn","nt",fasta_string)

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)

len(blast_record.alignments)

all_e = {}

E_VALUE_THRESH=0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            all_e[alignment.title] = hsp.expect

m = min(all_e.values())

# print mydict.keys()[mydict.values().index(16)]
print all_e.keys()[all_e.values().index(m)]