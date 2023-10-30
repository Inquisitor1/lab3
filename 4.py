import json
with open("firm.txt", "r", encoding="utf-8") as f:
    with open("firm.json", "w", encoding="utf-8") as f1:
        lines = f.readlines()
        pr_f = []
        d = {}
        for line in lines:
            data = line.strip().split()
            name = data[0]
            rev = int(data[2])
            cost = int(data[3])
            pr = rev - cost
            if pr > 0:
                pr_f.append(pr)
        ap = sum(pr_f)/len(pr_f) if pr_f else 0
        fin = [{"AP = ": ap}]
        for line in lines:
            data = line.strip().split()
            name = data[0]
            rev = int(data[2])
            cost = int(data[3])
            pr = rev - cost
            d[name] = pr
        fin.insert(0, d)
        print(fin)
        json.dump(fin, f1)
