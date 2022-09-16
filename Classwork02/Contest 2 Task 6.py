with open("/Classwork02/input.txt", "r", encoding="utf-8") as f:
    a = list(f.readlines())
nine_thebest = 0
ten_thebest = 0
eleven_thebest = 0
for i in range(len(a)):
    b = list(a[i].split())
    l_n, f_n, c, p = b
    c = int(c)
    p = int(p)
    if c == 9:
        if p > nine_thebest:
            nine_thebest = p 
    elif c == 10:
        if p > ten_thebest:
            ten_thebest = p
    else:
        if p > eleven_thebest:
            eleven_thebest = p
print(nine_thebest, ten_thebest, eleven_thebest, sep = ' ')
