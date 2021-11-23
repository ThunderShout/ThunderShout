print ("Quiz \nO teste possui 5 questões")
print ("1 - Qual a cor da casca de uma melancia completamente saudavel ?")
resp1 = str(input())
if resp1 == "verde":
    print("Correto!")
    totalptn = 1
else:
    print("Incorreto, a resposta correta é verde!")
    totalptn = 0

print("2 - Qual idade é considerada maioridade no brasil ?")
resp2 = int(input())
if resp2 == 18:
    print("Correto!")
    totalptn = totalptn +1
else:
    print("Incorreto, a resposta certa é 18")
    totalptn = totalptn -1

print("3 - Qual a sigla para associação brasileira de normas tecnicas ?")
resp3 = str(input())
if resp3 == "abnt":
    print("Correto!")
    totalptn = totalptn +1
else:
    print("Incorreto, a resposta certa é abnt")
    totalptn = totalptn -1

print("4 - Qual a função da memória de armazenamento ?")
resp4 = str(input())
if resp4 == "armazenar dados":
    print("Correto!")
    totalptn = totalptn +1
else:
    print("Incorreto, a resposta certa é armazenar dados")
    totalptn = totalptn -1

print("5 - Qual o DDD de são paulo ?")
resp5 = int(input())
if resp5 == 11:
    print("Correto!")
    totalptn = totalptn +1
else:
    print("Incorreto, a resposta certa é 11")
    totalptn = totalptn -1

print("Se chegou até aqui você esta no fim do teste, Parabéns!")
print("Veja agora sua pontuação")
print("Pontuação total:",totalptn)
input()
exit()