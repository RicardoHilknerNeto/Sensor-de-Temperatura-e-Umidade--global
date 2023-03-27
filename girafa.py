h1 = float(input("Digite a altura da girafa 1 em metros: "))
h2 = float(input("Digite a altura da girafa 2 em metros: "))
h3 = float(input("Digite a altura da girafa 3 em metros: "))
h4 = float(input("Digite a altura da girafa 4 em metros: "))
h5 = float(input("Digite a altura da girafa 5 em metros: "))

hei = 0

if h1 >= hei and h1 >= h2 and h1 >= h3 and h1 >= h4 and h1 >= h5:
    hei = h1
elif h2 >= hei and h1 >= h3 and h1 >= h4 and h1 >= h5:
    hei = h2
elif h3 >= hei and h1 >= h4 and h1 >= h5:
    hei = h3
elif h4 >= hei and h1 >= h5:
    hei = h4
else:
    hei = h5

print(f"A maior girafa tem {hei} metros")
