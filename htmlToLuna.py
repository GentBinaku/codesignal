from itertools import izip_longest
def htmlToLuna(html):
    html = html.replace(" ","")
    easyToProcessHtml = html.strip().replace("<img/>", "$i.").replace("</.{1,3}>", "/.").replace("<div>","d.").replace("<p>","p.").replace("<b>", "b.").replace('</b>','/b.').replace('</p>','/p.').replace('</div>','/d.')
    d = ""
    ReverseTags = {
        'd':'/d',
        'p':'/p',
        'b':'/b',
    }
    LookupTable = {
       'd':'DIV([',
        '/d': '])',
        'p' :'P([',
        '/p':'])',
        'b':'B([',
        '/b':'])',
        '$i':'IMG({})'
    }
    l = easyToProcessHtml.split(".")
    while('' in l):
         l.remove('')
    tail = False
    for fst, snd in izip_longest(l, l[1:], fillvalue='end'):
        if '/' in snd:
            d = d + LookupTable[fst]
            tail = True
        elif '/' not in snd:
            if tail:
             d = d + LookupTable[fst] + ', '
             tail = False
            else:
             d = d + LookupTable[fst]
        if fst == "$i" and '/' in snd:
            tail = False

    return d



html = "<div><p><img /></p><b></b></div>"
print htmlToLuna(html)