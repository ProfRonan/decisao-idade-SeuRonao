print("Digite um número")
idade = int(input("> "))

impossível = False
menor = False
maior = False
velho = False

if idade < 0:
    print("Impossível!")
    impossível = True
if idade < 18:
    print("Não precisa se alistar.")
    menor = True
if 18 < idade < 65:  # 18 < idade and idade < 65
    print("Não esqueça de votar na próxima eleição.")
    maior = True
if idade > 65:
    print("Vá descansar.")
    velho = True

if not (impossível or menor or maior or velho):
    print("Eita!")
