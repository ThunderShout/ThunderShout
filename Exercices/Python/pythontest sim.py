print ("questionário simples")
print ("O teste possui 10 questões\n Durante todo o teste você será informado quantas questões restam")
nl = 5
p = "a"
while nl != 1:
    nl = nl-1
    print(p)
    lres = str(input())
    if nl == 5:
        p = "Qual a Cor do Céu ?"
    elif nl == 4:
        p = "Qual a cor do sangue ?"
    elif nl == 3:
        p = "Com quantos anos se é considerado maior de idade ?"
    elif nl == 2:
        p = "Qual é a Cor da Casca da melancia ?"
    elif nl == 1:
        p = "qual o principal ingrediente do pão de batata ?"
