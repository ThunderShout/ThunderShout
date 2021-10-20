print ("Quiz \nO teste possui 5 questões")
nl = 5
ptn = 0
lres = None
while nl != 0:
    if nl == 5:
        print("Qual a Cor do Céu ?")
        if lres.islower() == "azul":
            print("resposta Correta!")
            ptn = ptn +1
        else:
            print("resposta Errada!")
    elif nl == 4:
        print("Qual a cor do sangue ?")
        if lres.islower() == "vermelho":
            print("Resposta Correta!")
            ptn = ptn +1
        else:
            print("Resposta Errada!")
    elif nl == 3:
        print("Com quantos anos se é considerado maior de idade ?")
        if lres == 18:
            print("Resposta Correta!")
            ptn = ptn +1
        else:
            print("Resposta Errada!")
    elif nl == 2:
        print("Qual é a Cor da Casca da melancia ?")
        if lres.islower() == "verde":
            print("Resposta Certa!")
            ptn = ptn +1
        else:
            print("Resposta Errada!")
    elif nl == 1:
        print("qual o principal ingrediente do pão de batata ?")
        if lres.islower() == "batata":
            print("Resposta Correta!")
            ptn = ptn +1
        else:
            print("Resposta Errada!")
    elif nl == 0:
        print("você acertou "+ptn+" questões")
        print("fim do teste!")
    nl = nl-1
