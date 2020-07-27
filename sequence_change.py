seq = "ATGTTATAG"

d = {'A':'T','T':'A','C':'G','G':'C'}
a = []
for i in list(seq):
    a.append(d[i])
print(''.join(a))
