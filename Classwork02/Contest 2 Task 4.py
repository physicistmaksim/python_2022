with open("text.txt", "r", encoding="utf-8") as f:
    a = list(f.readlines())
with open("text.txt", "w", encoding="utf-8") as f:
    for i in range(len(a)-1,-1,-1):
        f.writelines(a[i])