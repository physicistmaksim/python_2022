with open("/Classwork02/input9.txt", "r", encoding="utf-8") as f:
    a = list(f.readlines())
nine = 0
n_nine = 0
ten = 0
n_ten = 0
eleven = 0
n_eleven = 0
for i in range(len(a)):
    b = list(a[i].split())
    l_n, f_n, c, p = b
    c = int(c)
    p = int(p)
    if c == 9:
        nine += p
        n_nine += 1
    elif c == 10:
        ten += p
        n_ten += 1
    else:
        eleven += p
        n_eleven += 1
n = nine/n_nine
t = ten/n_ten
e = eleven/n_eleven
print(n, t, e, sep = ' ')
