with open("/Classwork02/input8.txt", "r", encoding="utf-8") as f:
    a = list(f.readlines())
people =[]
for i in range(len(a)):
    b = list(a[i].split())
    l_n, f_n, s, p = b
    s = int(s)
    p = int(p)
    people.append([l_n, f_n, p])
for i in range(len(people)):
    print(*sorted(people, key = lambda x: ord(x[0][0]))[i])
