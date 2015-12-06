dna = 'AGGTGACATTACCGCAAGCCTTATATTAGC'

def find_repeat(dna,n):
    L = len(dna)
    l = n
    substrings = {}
    for i in range(L-l+1):
        substring = dna[i:i+l]

        if substring not in substrings.keys():
            substrings[substring] = 1
        else:
            substrings[substring] += 1

    return substrings

substrings = find_repeat(dna,2)

m = max(substrings.values())
i = substrings.values().index(m)
seq = substrings.keys()[i]

print substrings
print seq, m


