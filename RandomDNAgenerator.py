import random

def create_dna(n,alphabet='ATCG'):
    return ''.join([random.choice(alphabet) for i in range(n)])
