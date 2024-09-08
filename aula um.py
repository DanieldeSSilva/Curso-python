SAUDACAO = "Olá! Seja bem vindo."
nome = input(f"{SAUDACAO} Qual é o seu nome?")
age = input(f"{SAUDACAO} Qual é o sua idade?")

data_nascimento = 2024-int(age)

if(int(age)>18):
    print(f"Voçê nasceu no ano de {data_nascimento} e já pode dirigir.")
    print(f"{nome} {age}")
    print(f"{nome} {age} ", end="...\n")    
    print(nome, age, sep="-")
else:
    print(f"Voçê nasceu no ano de {data_nascimento} e ainda não pode dirigir.")
    print("Teste String com aspas duplas")
    print('Teste String com aspas simples')
    print("Teste String com aspas 'simples' e \"duplas\"")

