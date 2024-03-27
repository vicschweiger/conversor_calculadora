def km_to_miles(km):
    miles = km * 0.621371
    return miles

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return celsius

def kg_to_pounds(kg):
    pounds = kg * 2.20462 
    return pounds

def mcg_to_mg(mcg):
    mg = mcg / 1000
    return mg

def mg_to_mcg(mg):
    mcg = mg * 1000
    return mcg

def imc(peso, altura):
    imc = peso / (altura * altura)
    return imc       
    

def menu():
    while True:
        entrada = int(input(
    """

    ##########################MENU##########################
            
            1. Quilômetros para milhas
            2. Celsius para Fahrenheit
            3. Quilograma para libras
            4. Micrograma (mcg) para miligrama (mg)
            5. Miligramas (mg) para microgramas (cmg)
            6. IMC
            0. Sair

    ########################################################
            
            Digite a opção escolhida:

    """

        ))
        if entrada == 0:
            print("Obrigado por usar nosso conversor, até breve!")
            break
        
        elif entrada == 1:
            km = int(input("Digite a quantidade de quilômetros: \n"))
            miles = km_to_miles(km)
            print(f"São {miles} milhas.")
        
        elif entrada == 2:
            celsius = int(input("Digite a temperatura em graus celsius: \n"))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"São {fahrenheit} graus.")
        
        elif entrada == 3:
            kg = float(input("Digite os quilos: \n"))
            pounds = kg_to_pounds(kg)
            print(f"São {pounds} kg.")
        
        elif entrada == 4:
            mcg = int(input("Digite o valor em microgramas (mcg): \n"))
            mg = mcg_to_mg(mcg)
            return print(f"São {mg}mg.")
        
        elif entrada == 5:
            mg = int(input("Digite o valor em miligramas (mg): \n"))
            mcg = mg_to_mcg(mg)
            print(f"São {mcg}mcg.")
        
        elif entrada == 6:
            peso = int(input("Digite seu peso: \n"))
            altura = float(input("Digite sua altura com ponto: \n"))
            resultado_imc = imc(peso, altura)
            print(f"Seu IMC é {resultado_imc}.")
            
            if resultado_imc >= 40:
                    print("Seu índice corpóreo é obesidade grau III.")
            elif resultado_imc >= 35:
                    print("Seu índice corpóreo é obesidade grau II.")
            elif resultado_imc >= 30:
                    print("Seu índice corpóreo é obesidade grau I.")   
            elif resultado_imc >= 25:
                    print("Seu índice corpóreo esta acima do peso.")
            elif resultado_imc >= 18.5:
                    print("Seu índice corpóreo esta normal.")
            elif resultado_imc >= 17:
                    print("Seu índice corpóreo esta abaixo do peso.")        
            else:
                print("Seu índice corpóreo esta muito abaixo do peso.") 
          
        else:
            print("Opção inválida!")
    
print(menu())