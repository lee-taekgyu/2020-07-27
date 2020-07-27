l1 = ['A','T','C','G']
l2 = ['A','T','C','G']

def kmer(l1,l2,n:int):
    l_total =[]
    if n ==1:
        return l2
    for i in l1:
        for j in l2:
            l_total.append(i+j)
    return kmer(l1, l_total, n-1)
import sys

n = int(sys.argv[1])
print(kmer(l1,l2,n))
