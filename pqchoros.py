# Função 




restaurantes ={

'Veg Veg':0,                        #Veg - Normal e Hamburguer - Ar Livre   
'Semente de Girassol': 0,           #Veg - Restaurante         - Fechado sul
'Restaurante Dom Veggie':0,         #Veg - Buffet              - Fechado oeste
'Bee.O':0 ,                         #Veg - Pizza               - Fechado oeste
'Famiglia Originale': 0 ,           #Veg - Pizza               - Fechado norte
'Love Vegan Pizza':0 ,              #Veg - Pizza               - Fechado central
'GreenGo':0 ,                       #Veg - Hamburguer          - Fechado    oeste
'Sorella':0 ,                       #Veg - Restaurante         - Fechado   oeste

'Churrascaria Batel Grill':0,       #Churrascaria - Família oeste
'Churrascaria Jardins Grill':0,     #Churrascaria - Família  sul
'Churrascaria Boi Dourado':0,       #Churrascaria - Família lest

'Mercado Sal':0 ,                   #Vários restaurantes - Família  - Ar livre
'Cadore':0 ,                        #Vários restaurantes - Família  - Ar livre norte
'Mercadoteca':0,                    #Vários restaurantes - Barzinho - Ar livre oeste
'Fresh Live Market':0,              #Vários restaurantes - Barzinho - Ar livre central
'Yamon':0,                          #Vários restaurantes - Barzinho - Ar Livre central
'Souq':0,                           #Vários restaurantes - Barzinho - Ar livre leste
'Sunset Cafe':0,                    #Vários restaurantes - Barzinho - Ar Livre norte

'Madalosso':0,                      #Típico - Família oeste
'Bar Do Alemao':0,                  #Típico - Barzinho central

'GeekCafe':0,                       #Hamburgueria - 

'Nuu Nikkei':0,                     #Japa - central 
'Taj Bar':0,                        #Japa - central
'Azuki':0,                          #Japa - norte

'Osteria Donna Lena':0,             #Italiano - Família - norte
'Ernesto':0,                        #Italiano - Família - norte
'Limoeiro Casa de Comidas':0,       #Italiano - Padrão  - norte
'Barolo Curitiba':0,                #Italiano - Padrão  - central

'Baggio':0,                         #Pizzaria - Família -  central
'Dom Carmino':0,                    #Pizzaria - Família -  central
'Avenida Paulista':0,               #Pizzaria - Família - central
 
}


# Pergunta comida vegana
res = int(input("Você tem preferencia por comidas veganas?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: "))

# Opções veganas de restaurante                 
if res == 1:
  restaurantes['Veg Veg'] +=1
  restaurantes['Restaurante Dom Veggie'] += 1
  restaurantes['Bee.O']+=1
  restaurantes['Famiglia Originale'] += 1
  restaurantes['Restaurante Dom Veggie'] +=1


# Pergunta pizza
res = int(input("Você gosta de Pizza?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: "))

# Opções restaurantes que servem pizza
if res == 1:
  restaurantes['Bee.O'] += 1
  restaurantes['Famiglia Originale'] +=1
  restaurantes['Avenida Paulista'] +=1
  restaurantes['Dom Carmino'] +=1
  restaurantes['Barolo Curitiba'] +=1
  restaurantes['Baggio'] +=1
  restaurantes['Love Vegan Pizza']+=1
  restaurantes['Mercado Sal'] +=1
  restaurantes['Mercadoteca'] +=1
  restaurantes['Fresh Live Market'] +=1
  restaurantes['Souq'] +=1

# Pergunta hamburgueria
res = int(input("Você gosta de Hamburgueria?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: ")) 

# Opções hamburguerias                  
if res == 1:
  restaurantes['Veg Veg'] +=1   
  restaurantes['GreenGo'] += 1
  restaurantes['GeekCafe'] +=1


# Pergunta restaurante italiano
res = int(input("Você gosta de comida italiana?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: "))  

# Opções restaurantes italianos
if res == 1:
    restaurantes['Limoeiro Casa de Comidas'] += 1
    restaurantes['Osteria Donna Lena'] +=1
    restaurantes['Ernesto'] += 1
    restaurantes['Barolo Curitiba'] += 1  
    

# Pergunta restaurante japonês
res = int(input("Você gosta de comida japonesa?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: "))

# Opções japonês               
if res ==1:
  restaurantes['Nuu Nikkei'] += 1                
  restaurantes['Taj Bar'] += 1                   
  restaurantes['Azuki'] += 1 


# Pergunta barzinhos    
res = int(input("Você gosta de Barzinho?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: "))  

# Opções barzinhos 
if res == 1:
  restaurantes['Yamon'] +=1
  restaurantes['Mercadoteca'] += 1              
  restaurantes['Fresh Live Market'] += 1         
  restaurantes['Souq'] +=1 
  restaurantes['Sunset Cafe'] += 1
  

# Pergunta filhos/família
res = int(input("Você tem filhos?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: "))   

# Opções restaurantes família
if res == 1:
  restaurantes['Churrascaria Jardins Grill'] +=1
  restaurantes['Churrascaria Boi Dourado'] +=1
  restaurantes['Mercado Sal'] +=1
  restaurantes['Cadore'] +=1



# Pergunta atividades em família
res = int(input("Você costuma praticar atividades em familia?\n"
              "[1] Sim\n"
              "[2] Não\n"
              "Digite sua opção: "))      

# Opções restaurantes familiares
if res == 1:
    restaurantes['Mercado Sal'] +=1
    restaurantes['Souq'] +=1
    restaurantes['Madalosso'] +=1
    restaurantes['Osteria Donna Lena'] +=1
    restaurantes['Ernesto'] +=1
    restaurantes['Barolo Curitiba'] +=1
    restaurantes['Baggio'] +=1
    restaurantes['Dom Carmino'] +=1
    restaurantes['Avenida Paulista'] +=1
    restaurantes['Azuki'] +=1
    restaurantes['Limoeiro Casa de Comidas'] +=1
 

# # Pergunta idade
# res = int(input("Qual sua idade?\n"
#                   "[1] 15-22\n"
#                   "[2] 23-35\n"
#                   "[3] 35-50\n"
#                   "[4] 50+\n"
#                   "Digite sua opção: "))   
                  
# # Opções restaurante por idade
                  
                  
# Pergunta show
res = int(input("Você gosta de show?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: "))

# Opções restaurantes com show
if res ==1:
  restaurantes['Souq'] +=1
  restaurantes['Mercado Sal'] += 1
  
  
# Pergunta hábitos saudáveis
res = int(input("Você possui habitos saudáveis?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: "))

# Opções restaurantes com comida saudável
if res == 1:
  restaurantes['Veg Veg'] += 1                   
  restaurantes['Semente de Girassol'] +=1       
  restaurantes['Restaurante Dom Veggie'] +=1      
  restaurantes['Bee.O'] +=1                  
  restaurantes['Famiglia Originale'] +=1      
  restaurantes['Love Vegan Pizza'] +=1         
  restaurantes['GreenGo'] +=1                
  restaurantes['Sorella'] +=1 
  restaurantes['Nuu Nikkei'] +=1                 
  restaurantes['Taj Bar'] +=1                   
  
 
# Pergunta animais de estimação
res = int(input("Você possui animais de estimação?\n"
                  "[1] Sim\n"
                  "[2] Não\n"
                  "Digite sua opção: "))   
 
# Opções com área pra animais
if res == 1:
    restaurantes['Veg Veg'] +=1
    restaurantes['Mercado Sal'] +=1
    restaurantes['Cadore'] +=1
    restaurantes['Mercadoteca'] +=1
    restaurantes['Yamon'] +=1
    restaurantes['Souq'] +=1
    restaurantes['Sunset Cafe'] +=1
    restaurantes['Limoeiro Casa de Comidas'] +=1

# Pergunta região da cidade
res = int(input("Você mora na região\n"
                  "[1] Norte\n"
                  "[2] Sul\n"
                  "[3] Leste\n"
                  "[4] Oeste\n"
                  "[5] Central\n"
                  "Digite sua opção: "))   

# Opções região
if res == 1:
    restaurantes['Sunset Cafe'] += 1
    restaurantes['Famiglia Originale'] += 1
    restaurantes['Azuki']+= 1
    restaurantes['Osteria Donna Lena'] += 1
    restaurantes['Ernesto'] += 1                  
    restaurantes['Limoeiro Casa de Comidas'] += 1

elif res == 2:
    restaurantes['Mercado Sal'] += 1
    restaurantes['Churrascaria Jardins Grill'] += 1
    restaurantes['Semente de Girassol'] += 1

elif res == 3:
    restaurantes['Churrascaria Boi Dourado'] += 1
    restaurantes['Souq'] += 1

elif res == 4:
    restaurantes['Veg Veg'] += 1
    restaurantes['Restaurante Dom Veggie'] += 1
    restaurantes['Bee.O'] += 1
    restaurantes['GreenGo'] += 1
    restaurantes['Sorella'] += 1
    restaurantes['Churrascaria Batel Grill'] += 1
    restaurantes['Mercadoteca'] += 1
    restaurantes['Madalosso'] += 1

else:
    restaurantes['Semente de Girassol'] += 1
    restaurantes['GeekCafe'] +=1
    restaurantes['Love Vegan Pizza'] +=1
    restaurantes['Fresh Live Market'] +=1
    restaurantes['Yamon'] +=1
    restaurantes['Bar Do Alemao'] +=1
    restaurantes['Nuu Nikkei'] +=1
    restaurantes['Taj Bar'] +=1
    restaurantes['Barolo Curitiba'] +=1
    restaurantes['Barolo Curitiba'] +=1
    restaurantes['Baggio'] +=1
    restaurantes['Dom Carmino'] +=1
    restaurantes['Avenida Paulista'] +=1
 


# Pergunta horário de dormir
res = int(input("Você dorme cedo?\n"
              "[1] Sim\n"
              "[2] Não\n"
              "Digite sua opção: "))  

# Opções restaurantes que abrem mais cedo
if res ==1:
  restaurantes['Mercado Sal'] += 1
  restaurantes['Mercadoteca'] += 1              
  restaurantes['Souq'] +=1
  restaurantes['Azuki'] += 1
  restaurantes['Limoeiro Casa de Comidas'] += 1
  restaurantes['GeekCafe'] += 1
    

     
# # Pergunta gasto financeiro
res = int(input("Quanto você gasta em media em resutaurantes (por pessoa)?\n"
                "[1] R$ 30,00 - R$ 50,00\n"
                "[2] R$ 50,00 - R$ 100,0 \n"
                "[3] R$ R$ 100,0 - R$150,00 \n"
                "[4] R$150,00 + \n"
                "Digite sua opção: "))    
if res == 1:
  restaurantes['Semente de Girassol'] += 1

elif res == 2:
  restaurantes['Veg Veg'] += 1
  restaurantes['Restaurante Dom Veggie'] += 1
  restaurantes['Faniglia Originale'] += 1
  restaurantes['Love Vegan Pizza'] += 1
  restaurantes['GreenGo'] += 1
  restaurantes['Sorella'] += 1
  restaurantes['Churrascaria  Boi Dourado'] += 1
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
  
elif res == 3:
  restaurantes['Bee.O'] += 1
  restaurantes['Churrascaria Jardins Grill'] += 1
  restaurantes['Cadore'] += 1
  restaurantes['Mercadoteca'] += 1
  restaurantes['Madalosso'] += 1
  restaurantes['Bar Do Alemão'] += 1
  restaurantes['Taj Bar'] += 1
  restaurantes['Nuu Nikkei'] += 1
  restaurantes['Azuki'] += 1
  restaurantes['Ernesto'] += 1
  restaurantes['Barolo Curitiba'] += 1
  restaurantes['Avenida Paulista'] += 1
  
else:
 restaurantes['Churrascaria Batel Grill'] += 1


for keys in restaurantes.keys():
  if restaurantes[keys] >= 10:
    print("Você mais probabilidade de gotas desse retaurante: "+ keys )
  elif restaurantes[keys] >=5:
    print(f"Restaurantes com 5: {keys}")
                
