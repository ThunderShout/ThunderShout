name = input("digite o nome do funcionário:")
name2 = input("digite o nome de outro funcionário:")
name3 = input("digite o nome de um terceiro funcionário:")
i = 0
calculo1 = 0
calculo2 = 0
calculo3 = 0
while i < 12:
    n1 = input("digite o numero de vendas do funcionário {} no mês :".format(name))
    n2 = input("digite o numero de vendas do funcionário {} no mês :".format(name2))
    n3 = input("digite o numero de vendas do funcionário {} no mês :".format(name3))
    n1 =int(n1)
    n2 =int(n2)
    n3 =int(n3)
    calculo1 = calculo1 + n1
    calculo2 = calculo2 + n2
    calculo3 = calculo3 + n3
    i += 1
else: 
    calculo1 = calculo1/12
    calculo2 = calculo2/12
    calculo3 = calculo3/12
    print("a média de vendas anual do vendedor {} é: {}".format(name,calculo1))
    print("a média de vendas anual do vendedor {} é: {}".format(name2,calculo2))
    print("a média de vendas anual do vendedor {} é: {}".format(name3,calculo3))