kalimat = input('Masukkan kalimat :')
insensitive = kalimat.lower()
a = insensitive.split()
n = 0
kata = input('Masukkan satu kata :')
for i in a:
    if kata == i:
        n+=1
print(n)