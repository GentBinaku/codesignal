import collections
import re
def packetDescrambler(seq, fragmentData, n):
    d = {}
    s = []
    r = ""
    for i,x in enumerate(seq):
        if x not in s:
            d[x] = [fragmentData[i]]
            s.append(x)
        else:
            d[x].append(fragmentData[i])
    for c in d.values():
        for i in list(collections.Counter(c).items()):
             if float(i[1])/n > 0.5:
                 r = r + str(i[0])
                 break
    if not re.match(r"^[^#]+",r) or len(set(seq)) != len(r):
                return ""
    return r


print packetDescrambler([1, 1, 2, 2, 2, 4, 4],["+", "+","A","A","B", "#", "#"],n = 4)