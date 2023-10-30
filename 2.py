with open("client.txt", "r") as f:
    lines = []
    for line in f:
        lines.append(line.split())
    print(lines)
    max_val = []
    maxi = int(lines[0][1])
    maxi_val = []
    for i in lines:
        k = int(i[1])
        if k > maxi:
            maxi = k
            maxi_val = i
        if k >= 1000:
            max_val.append(i)
    print(f"\nКлиент, с наибольшей суммой на счету: ", maxi_val[0])
    print(f"Клиенты, с суммой больше 1000 на счету: ", *max_val)