print("exercício de loop de tabuada")
n1 = input("insira um numero para ser a base da tabuada:")
n2 = input("insira um limite para a tabuada:")
l = 0
n1 = float(n1)
n2 = float(n2)
if n2 > 9000:
    n2 = 9000
    input("O limite inserido foi reestabelecido para 9000 por ser muito alto")
while l <= n2:
    n3 = n1*l
    print("{} X {} = {}".format(n1,l,n3))
    l += 1
else:
    print("fim da tabuada")