def calculoPorcentagem(value, perguntasFeitas):
    value = (100*value)/perguntasFeitas
    return value



contBar = 0

perguntasFeitas = 0
# <-------Objeto------>

restaurantes = {

    'Veg Veg': 0,  # Veg - Normal e Hamburguer - Ar Livre
    'Semente de Girassol': 0,  # Veg - Restaurante         - Fechado sul
    'Restaurante Dom Veggie': 0,  # Veg - Buffet              - Fechado oeste
    'Bee.O': 0,  # Veg - Pizza               - Fechado oeste
    'Famiglia Originale': 0,  # Veg - Pizza               - Fechado norte
    'Love Vegan Pizza': 0,  # Veg - Pizza               - Fechado central
    'GreenGo': 0,  # Veg - Hamburguer          - Fechado    oeste
    'Sorella': 0,  # Veg - Restaurante         - Fechado   oeste

    'Churrascaria Batel Grill': 0,  # Churrascaria - Família oeste
    'Churrascaria Jardins Grill': 0,  # Churrascaria - Família  sul
    'Churrascaria Boi Dourado': 0,  # Churrascaria - Família lest

    'Mercado Sal': 0,  # Vários restaurantes - Família  - Ar livre
    'Cadore': 0,  # Vários restaurantes - Família  - Ar livre norte
    'Mercadoteca': 0,  # Vários restaurantes - Barzinho - Ar livre oeste
    'Fresh Live Market': 0,  # Vários restaurantes - Barzinho - Ar livre central
    'Yamon': 0,  # Vários restaurantes - Barzinho - Ar Livre central
    'Souq': 0,  # Vários restaurantes - Barzinho - Ar livre leste
    'Sunset Cafe': 0,  # Vários restaurantes - Barzinho - Ar Livre norte

    'Madalosso': 0,  # Típico - Família oeste
    'Bar Do Alemao': 0,  # Típico - Barzinho central

    'GeekCafe': 0,  # Hamburgueria -

    'Nuu Nikkei': 0,  # Japa - central
    'Taj Bar': 0,  # Japa - central
    'Azuki': 0,  # Japa - norte

    'Osteria Donna Lena': 0,  # Italiano - Família - norte
    'Ernesto': 0,  # Italiano - Família - norte
    'Limoeiro Casa de Comidas': 0,  # Italiano - Padrão  - norte
    'Barolo Curitiba': 0,  # Italiano - Padrão  - central

    'Baggio': 0,  # Pizzaria - Família -  central
    'Dom Carmino': 0,  # Pizzaria - Família -  central
    'Avenida Paulista': 0,  # Pizzaria - Família - central

}

# # Pergunta idade
resIdade = int(input("Qual sua idade?\n"
                     "[1] 15-22\n"
                     "[2] 23-35\n"
                     "[3] 35-50\n"
                     "[4] 50+\n"
                     "Digite sua opção: "))
perguntasFeitas +=1

# Se a pessoa tem entre 15 e 22 anos, selecionar essas opções:
if resIdade == 1:
    restaurantes['Souq'] += 1
    restaurantes['Mercado Sal'] += 1
    restaurantes['Mercadoteca'] += 1
    restaurantes['Fresh Live Market'] += 1
    restaurantes['Sunset Cafe'] += 1
    restaurantes['GeekCafe'] += 1

# Se a pessoa tem entre 23 e 35 anos, selecionar essas opções:
elif resIdade == 2:
    restaurantes['Souq'] += 1
    restaurantes['Mercado Sal'] += 1
    restaurantes['Mercadoteca'] += 1
    restaurantes['Fresh Live Market'] += 1
    restaurantes['Sunset Cafe'] += 1
    restaurantes['GeekCafe'] += 1
    restaurantes['Veg Veg'] += 1
    restaurantes['Nuu Nikkei'] += 1
    restaurantes['Limoeiro Casa de Comidas'] += 1
    restaurantes['Avenida Paulista'] += 1
    restaurantes['Bar Do Alemao'] += 1
    restaurantes['Baggio'] += 1
    restaurantes['Azuki'] += 1
    restaurantes['Taj Bar'] += 1

# Se a pessoa tem entre 35 e 50 anos, selecionar essas opções:
elif resIdade == 3:
    restaurantes['Veg Veg'] += 1
    restaurantes['Nuu Nikkei'] += 1
    restaurantes['Limoeiro Casa de Comidas'] += 1
    restaurantes['Avenida Paulista'] += 1
    restaurantes['Bar Do Alemao'] += 1
    restaurantes['Baggio'] += 1
    restaurantes['Azuki'] += 1
    restaurantes['GreenGo'] += 1

# Se a pessoa tem mais de 50 anos, selecionar essas opções:
elif resIdade == 4:
    restaurantes['Churrascaria Batel Grill'] += 1
    restaurantes['Churrascaria Jardins Grill'] += 1
    restaurantes['Churrascaria Boi Dourado'] += 1
    restaurantes['Azuki'] += 1
    restaurantes['Bar Do Alemao'] += 1
    restaurantes['Baggio'] += 1
    restaurantes['Madalosso'] += 1
    restaurantes['Barolo Curitiba'] += 1
    restaurantes['Ernesto'] += 1
    restaurantes['Famiglia Originale'] += 1

# Se a pessoa tem mais do que 22 anos, fazer essa pergunta:
if resIdade == 2:
   # Pergunta atividades em família
    resFamilia = int(input("Você costuma praticar atividades em familia?\n"
                           "[1] Sim\n"
                           "[2] Não\n"
                           "Digite sua opção: "))
    perguntasFeitas +=1

    # Se a pessoa gosta de atividades em família, fazer essa pergunta:
    if resFamilia == 1:

      # Se a pessoa gosta de atividades em família, selecionar essas opções:
        restaurantes['Mercado Sal'] += 1
        restaurantes['Souq'] += 1
        restaurantes['Madalosso'] += 1
        restaurantes['Osteria Donna Lena'] += 1
        restaurantes['Ernesto'] += 1
        restaurantes['Barolo Curitiba'] += 1
        restaurantes['Baggio'] += 1
        restaurantes['Dom Carmino'] += 1
        restaurantes['Avenida Paulista'] += 1
        restaurantes['Azuki'] += 1
        restaurantes['Limoeiro Casa de Comidas'] += 1

      # Pergunta filhos/família
        resFilho = int(input("Você tem filhos?\n"
                             "[1] Sim\n"
                             "[2] Não\n"
                             "Digite sua opção: "))
        perguntasFeitas +=1

        # Se a pessoa tem filhos, selecionar essas opções:
        if resFilho == 1:
            restaurantes['Churrascaria Jardins Grill'] += 1
            restaurantes['Churrascaria Boi Dourado'] += 1
            restaurantes['Mercado Sal'] += 1
            restaurantes['Cadore'] += 1

    # Se a pessoa gosta de atividades em família, fazer essa pergunta:
    if resFamilia == 1 and resFilho == 1:
        # Pergunta animais de estimação
        resAnimal = int(input("Você possui animais de estimação?\n"
                              "[1] Sim\n"
                                "[2] Não\n"
                                "Digite sua opção: "))
        perguntasFeitas +=1

        # Se a pessoa possui animais de estimação, selecionar essas opções:
        if resAnimal == 1:
            restaurantes['Veg Veg'] += 1
            restaurantes['Mercado Sal'] += 1
            restaurantes['Cadore'] += 1
            restaurantes['Mercadoteca'] += 1
            restaurantes['Yamon'] += 1
            restaurantes['Souq'] += 1
            restaurantes['Sunset Cafe'] += 1
            restaurantes['Limoeiro Casa de Comidas'] += 1

    # Se a pessoa não gosta de atividades em família, fazer essa pergunta:
    elif resFamilia == 2 and contBar < 1:
        # Pergunta barzinhos
        resBar = int(input("Você gosta de Barzinho?\n"
                           "[1] Sim\n"
                           "[2] Não\n"
                           "Digite sua opção: "))
        perguntasFeitas +=1

        # Se a pessoa gosta de barzinho, selecionar essas opções:
        if resBar == 1:
            contBar +=1
            restaurantes['Yamon'] += 1
            restaurantes['Mercadoteca'] += 1
            restaurantes['Fresh Live Market'] += 1
            restaurantes['Souq'] += 1
            restaurantes['Sunset Cafe'] += 1
          # Pergunta restaurante japonês

          # Se a pessoa gosta de restaurante japonês, selecionar essas opções:
        if resBar == 2:
            contBar+=1
            restaurantes['Nuu Nikkei'] += 1
            restaurantes['Taj Bar'] += 1
            restaurantes['Azuki'] += 1

# Se a pessoa tem entre 15 e 22 anos ou entre 23 e 35, fazer essa pergunta:
if resIdade == 1 or resIdade == 2 and contBar < 1:
  resBar = int(input("Você gosta de Barzinho?\n"
                      "[1] Sim\n"
                          "[2] Não\n"
                          "Digite sua opção: "))
  perguntasFeitas +=1

  # Se a pessoa gosta de barzinho, selecionar essas opções:
  if resBar == 1:
      restaurantes['Yamon'] += 1
      restaurantes['Mercadoteca'] += 1
      restaurantes['Fresh Live Market'] += 1
      restaurantes['Souq'] += 1
      restaurantes['Sunset Cafe'] += 1

      # Pergunta sobre shows
      resShow = int(input("Você gosta de show?\n"
                          "[1] Sim\n"
                          "[2] Não\n"
                          "Digite sua opção: "))

      # Se a pessoa gosta de show, selecionar essas opções:
      if resShow == 1:
          restaurantes['Souq'] += 1
          restaurantes['Mercado Sal'] += 1

  elif resBar == 2:
      pass


# ------------------------------------------------


# Se a pessoa tem entre 35 e 50 anos ou mais de 50 anos, fazer essa pergunta:
if resIdade == 4 or resIdade == 3:
       # Pergunta hábitos saudáveis
    resSaude = int(input("Você possui habitos saudáveis?\n"
                         "[1] Sim\n"
                         "[2] Não\n"
                         "Digite sua opção: "))
    perguntasFeitas +=1


    # Se a pessoa possui hábitos saudáveis, fazer essa pergunta:
    if resSaude == 1:
           # Se a pessoa possui hábitos saudáveis, selecionar essas opções:
        restaurantes['Veg Veg'] += 1
        restaurantes['Semente de Girassol'] += 1
        restaurantes['Restaurante Dom Veggie'] += 1
        restaurantes['Bee.O'] += 1
        restaurantes['Famiglia Originale'] += 1
        restaurantes['Love Vegan Pizza'] += 1
        restaurantes['GreenGo'] += 1
        restaurantes['Sorella'] += 1
        restaurantes['Nuu Nikkei'] += 1
        restaurantes['Taj Bar'] += 1
        # Pergunta comida vegana
        resVeg = int(input("Você tem preferencia por comidas veganas?\n"
                           "[1] Sim\n"
                           "[2] Não\n"
                           "Digite sua opção: "))
        perguntasFeitas +=1

        # Se a pessoa tem preferência sobre comidas veganas, selecionar essas opções:
        if resVeg == 1:
            restaurantes['Veg Veg'] += 1
            restaurantes['Restaurante Dom Veggie'] += 1
            restaurantes['Bee.O'] += 1
            restaurantes['Famiglia Originale'] += 1
            restaurantes['Restaurante Dom Veggie'] += 1


        # Se a pessoa não tem preferência sobre comidas veganas, perguntar sobre hamburgueria
        if resSaude == 2:

            # Se a pessoa não tem preferência sobre comidas veganas, selecionar essas opções:
            restaurantes['Churrascaria Batel Grill'] += 1
            restaurantes['Churrascaria Jardins Grill'] += 1

            # Pergunta hamburgueria
            resHamburger = int(input("Você gosta de Hamburgueria?\n"
                                     "[1] Sim\n"
                                     "[2] Não\n"
                                     "Digite sua opção: "))
            perguntasFeitas +=1

            # Se a pessoa gosta de hamburguerias, selecionar essas opções:
            if resHamburger == 1:
                restaurantes['Veg Veg'] += 1
                restaurantes['GreenGo'] += 1
                restaurantes['GeekCafe'] += 1

            elif resHamburger == 2:
                # Pergunta pizza
                resPizza = int(input("Você gosta de Pizza?\n"
                                     "[1] Sim\n"
                                     "[2] Não\n"
                                     "Digite sua opção: "))
                perguntasFeitas +=1

                # Se a pessoa gosta de pizza, selecionar essas opções:
                if resPizza == 1:
                    restaurantes['Bee.O'] += 1
                    restaurantes['Famiglia Originale'] += 1
                    restaurantes['Avenida Paulista'] += 1
                    restaurantes['Dom Carmino'] += 1
                    restaurantes['Barolo Curitiba'] += 1
                    restaurantes['Baggio'] += 1
                    restaurantes['Love Vegan Pizza'] += 1
                    restaurantes['Mercado Sal'] += 1
                    restaurantes['Mercadoteca'] += 1
                    restaurantes['Fresh Live Market'] += 1
                    restaurantes['Souq'] += 1


# Se a pessoa tem entre 35 e 50 anos ou mais de 50 anos, fazer essa pergunta:
if resIdade == 3 or resIdade == 4:
    # Pergunta horário de dormir
    resHorario = int(input("Você dorme cedo?\n"
                           "[1] Sim\n"
                           "[2] Não\n"
                           "Digite sua opção: "))
    perguntasFeitas +=1

    # Se a pessoa dorme cedo, selecionar essas opções:
    if resHorario == 1:
        restaurantes['Mercado Sal'] += 1
        restaurantes['Mercadoteca'] += 1
        restaurantes['Souq'] += 1
        restaurantes['Azuki'] += 1
        restaurantes['Limoeiro Casa de Comidas'] += 1
        restaurantes['GeekCafe'] += 1

# Pergunta restaurante italiano
resItaliana = int(input("Você gosta de comida italiana?\n"
                        "[1] Sim\n"
                        "[2] Não\n"
                        "Digite sua opção: "))
perguntasFeitas +=1


# Se a pessoa gosta de comida italiana, selecionar essas opções:
if resItaliana == 1:
    restaurantes['Limoeiro Casa de Comidas'] += 1
    restaurantes['Osteria Donna Lena'] += 1
    restaurantes['Ernesto'] += 1
    restaurantes['Barolo Curitiba'] += 1
    # Pergunta pizza
    resPizza = int(input("Você gosta de Pizza?\n"
                         "[1] Sim\n"
                         "[2] Não\n"
                         "Digite sua opção: "))
    perguntasFeitas +=1

    # Se a pessoa gosta de pizza, selecionar essas opções:
    if resPizza == 1:
        restaurantes['Bee.O'] += 1
        restaurantes['Famiglia Originale'] += 1
        restaurantes['Avenida Paulista'] += 1
        restaurantes['Dom Carmino'] += 1
        restaurantes['Barolo Curitiba'] += 1
        restaurantes['Baggio'] += 1
        restaurantes['Love Vegan Pizza'] += 1
        restaurantes['Mercado Sal'] += 1
        restaurantes['Mercadoteca'] += 1
        restaurantes['Fresh Live Market'] += 1
        restaurantes['Souq'] += 1


# Se a pessoa NÃO gosta de comida italiana, fazer essa pergunta:
if resItaliana == 2:
  pass


# Pergunta região da cidade
resRegiao = int(input("Você mora na região\n"
                "[1] Norte\n"
                "[2] Sul\n"
                "[3] Leste\n"
                "[4] Oeste\n"
                "[5] Central\n"
                "Digite sua opção: "))
perguntasFeitas +=1

# Se a pessoa mora na região NORTE, selecionar essas opções:
if resRegiao == 1:
    restaurantes['Sunset Cafe'] += 1
    restaurantes['Famiglia Originale'] += 1
    restaurantes['Azuki'] += 1
    restaurantes['Osteria Donna Lena'] += 1
    restaurantes['Ernesto'] += 1
    restaurantes['Limoeiro Casa de Comidas'] += 1

# Se a pessoa mora na região SUL, selecionar essas opções:
elif resRegiao == 2:
    restaurantes['Mercado Sal'] += 1
    restaurantes['Churrascaria Jardins Grill'] += 1
    restaurantes['Semente de Girassol'] += 1

# Se a pessoa mora na região LESTE, selecionar essas opções:
elif resRegiao == 3:
    restaurantes['Churrascaria Boi Dourado'] += 1
    restaurantes['Souq'] += 1

# Se a pessoa mora na região OESTE, selecionar essas opções:
elif resRegiao == 4:
    restaurantes['Veg Veg'] += 1
    restaurantes['Restaurante Dom Veggie'] += 1
    restaurantes['Bee.O'] += 1
    restaurantes['GreenGo'] += 1
    restaurantes['Sorella'] += 1
    restaurantes['Churrascaria Batel Grill'] += 1
    restaurantes['Mercadoteca'] += 1
    restaurantes['Madalosso'] += 1

# Se a pessoa mora na região CENTRAL, selecionar essas opções:
else:
    restaurantes['Semente de Girassol'] += 1
    restaurantes['GeekCafe'] += 1
    restaurantes['Love Vegan Pizza'] += 1
    restaurantes['Fresh Live Market'] += 1
    restaurantes['Yamon'] += 1
    restaurantes['Bar Do Alemao'] += 1
    restaurantes['Nuu Nikkei'] += 1
    restaurantes['Taj Bar'] += 1
    restaurantes['Barolo Curitiba'] += 1
    restaurantes['Barolo Curitiba'] += 1
    restaurantes['Baggio'] += 1
    restaurantes['Dom Carmino'] += 1
    restaurantes['Avenida Paulista'] += 1

# Pergunta gasto financeiro
resValor = int(input("Quanto você gasta em media em resutaurantes (por pessoa)?\n"
                     "[1] R$ 30,00 - R$ 50,00\n"
                     "[2] R$ 50,00 - R$ 100,0 \n"
                     "[3] R$ R$ 100,0 - R$150,00 \n"
                     "[4] R$150,00 + \n"
                     "Digite sua opção: "))
perguntasFeitas +=1

# Se a pessoa pretende gastar entre 30 e 50 reais, selecionar essas opções:
if resValor == 1:
    restaurantes['Semente de Girassol'] += 1

# Se a pessoa pretende gastar entre 50 e 100 reais, selecionar essas opções:
elif resValor == 2:
    restaurantes['Veg Veg'] += 1
    restaurantes['Restaurante Dom Veggie'] += 1
    restaurantes['Famiglia Originale'] += 1
    restaurantes['Love Vegan Pizza'] += 1
    restaurantes['GreenGo'] += 1
    restaurantes['Sorella'] += 1
    restaurantes['Churrascaria Boi Dourado'] += 1
    restaurantes['Mercado Sal'] += 1
    restaurantes['Fresh Live Market'] += 1
    restaurantes['Yamon'] += 1
    restaurantes['Souq'] += 1
    restaurantes['Sunset Cafe'] += 1
    restaurantes['GeekCafe'] += 1
    restaurantes['Osteria Donna Lena'] += 1
    restaurantes['Limoeiro Casa de Comidas'] += 1
    restaurantes['Baggio'] += 1
    restaurantes['Dom Carmino'] += 1

# Se a pessoa pretende gastar entre 100 e 150 reais, selecionar essas opções:
elif resValor == 3:
    restaurantes['Bee.O'] += 1
    restaurantes['Churrascaria Jardins Grill'] += 1
    restaurantes['Cadore'] += 1
    restaurantes['Mercadoteca'] += 1
    restaurantes['Madalosso'] += 1
    restaurantes['Bar Do Alemao'] += 1
    restaurantes['Taj Bar'] += 1
    restaurantes['Nuu Nikkei'] += 1
    restaurantes['Azuki'] += 1
    restaurantes['Ernesto'] += 1
    restaurantes['Barolo Curitiba'] += 1
    restaurantes['Avenida Paulista'] += 1

# Se a pessoa pretende gastar mais de 150 reais, selecionar essas opções:
else:
    restaurantes['Churrascaria Batel Grill'] += 1


# Array ordenado de acordo com a pontuação
ordenado = sorted(restaurantes.items(), key=lambda item: item[1], reverse=True)

for i in ordenado:
    for a in range(3):
        if a > 1:
            value = calculoPorcentagem(i[1], perguntasFeitas)
            if value > 0:
              print(f"Você gostaria do {i[0]}, com a porcetagem {value:.2F}%")
