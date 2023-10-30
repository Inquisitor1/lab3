with open("pary.txt", "r", encoding="utf-8") as f:

    d = {}
    d1 = {}
    lifinal = []
    while True:
        li = f.readline()
        if not li:
            break
        spis = li.split(' ')
        i = 1
        while i < len(spis):
            spis1 = list(spis[i])
            ind1 = spis1.index('(')
            ch = int(spis[i][0:ind1])
            lifinal.append(ch)
            i += 1
        d1[spis[0]] = sum(lifinal)
        d.update(d1)
        print(d)

