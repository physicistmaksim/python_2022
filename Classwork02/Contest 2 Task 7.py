with open("input7.txt", "r", encoding="utf-8") as f:
    a = list(f.readlines())
schools = []
alr = True
for i in range(len(a)):
    b = list(a[i].split())
    l_n, f_n, s, p = b
    s = int(s)
    p = int(p)
    if p > 70:
        for i in schools:
            if i == s:
                alr = False
        if alr:
            schools.append(s)
        alr = True
print(*schools)
