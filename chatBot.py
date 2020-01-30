from operator import itemgetter
def chatBot(conversations, currentConversation):
    d = [list(f7(c)) for c in conversations]
    s = []
    ca = []
    for w in d:
        count = 0
        for c in w:
                if c in list(currentConversation):
                    count += 1
        s.append((w,count))
        ca.append(count)
    if(len(set(ca)) == 1): return currentConversation
    word = max(s,key=itemgetter(1))[0][::-1]
    a = []
    for c in word:
        if c not in currentConversation:
            a.append(c)
        else:
            break
    a = a[::-1]
    currentConversation.extend(a)
    return currentConversation




def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

print chatBot([
     ["lets", "have", "some", "fun"],
     ["i", "never", "get", "it"],
     ["be", "aware", "of", "this", "house"],
     ["he", "will", "call", "her"]
 ],["can","you", "please"])