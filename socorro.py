restaurantes = {'VegVeg': 0 ,                    
'SementedeGirassol':0 ,    
'RestauranteDomVeggie':0,     
'Bee.    O': 5,                  
'FamigliaOriginale': 0,     
'LovePizzaVegan': 1    ,       
'Green Go': 5 ,              
'Sorella':0}   

restaurantes['VegVeg'] = 1


for akey in restaurantes.keys():  
    if restaurantes[akey] > 3:   
        print("UHULLLL   " + akey)
    elif  restaurantes[akey] <= 3:
        print("AAAAAAAAAAAAAAAAAAA   " + akey)