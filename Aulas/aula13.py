# formatação de strings que com metodo format
a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={nome3}'
formato = string.format(
    a, b, nome3=c
)

print(formato)
print('"Já sei!"')
