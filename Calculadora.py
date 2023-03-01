
nome = str(input("Olá, qual seu nome? \n"))
print("Muito bem "+ nome+", vamos começar! \n")

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor valor: "))

inicio = 1

while inicio == 1:
    operacao = input(str("Qual operação deseja fazer? (+ , - , * , /) \n"))
    if operacao == "+":
        n3 = n1 + n2
        print(n3)
        inicio = int(input("""Como deseja prosseguir: 
                           [1] Realizar uma nova conta
                           [2] Continuar com resultado anterior
                           [3] Finalizar programa \n"""))
        
    elif operacao == "-":
        n3 = n1 - n2
        print(n3)
        inicio = int(input("""Como deseja prosseguir: 
                           [1] Realizar uma nova conta
                           [2] Continuar com resultado anterior
                           [3] Finalizar programa \n"""))
        
    elif operacao == "*":
        n3 = n1 * n2
        print(n3)
        inicio = int(input("""Como deseja prosseguir: 
                           [1] Realizar uma nova conta
                           [2] Continuar com resultado anterior
                           [3] Finalizar programa \n"""))
        
    elif operacao == "/":
        n3 = n1 / n2
        print(n3)
        inicio = int(input("""Como deseja prosseguir: 
                           [1] Realizar uma nova conta
                           [2] Continuar com resultado anterior
                           [3] Finalizar programa \n"""))

    else:
        print("Não foi possivel realizar o calculo")
        
while inicio == 2:
    operacao = input(str("Qual operação deseja fazer? (+ , - , * , /) \n"))
    n4 = float(input("Qual o segundo numero a ser calculado? "))
    
    if operacao == "+":
        n3 += n4
        print(n3)
        inicio = int(input("""Como deseja prosseguir: 
                           [1] Realizar uma nova conta
                           [2] Continuar com resultado anterior
                           [3] Finalizar programa \n"""))
        
    elif operacao == "-":
        n3 -= n4
        print(n3)
        inicio = int(input("""Como deseja prosseguir: 
                           [1] Realizar uma nova conta
                           [2] Continuar com resultado anterior
                           [3] Finalizar programa \n"""))
        
    elif operacao == "*":
        n3 *= n4
        print(n3)
        inicio = int(input("""Como deseja prosseguir: 
                           [1] Realizar uma nova conta
                           [2] Continuar com resultado anterior
                           [3] Finalizar programa \n"""))
        
    elif operacao == "/":
        n3 /= n4
        print(n3)
        inicio = int(input("""Como deseja prosseguir: 
                           [1] Realizar uma nova conta
                           [2] Continuar com resultado anterior
                           [3] Finalizar programa \n"""))

    else:
        print("Não foi possivel realizar o calculo")
        inicio = int(input("""Como deseja prosseguir: 
                           [1] Realizar uma nova conta
                           [2] Continuar com resultado anterior
                           [3] Finalizar programa \n"""))

while inicio == 3:
    print("Obrigado, até mais")
    inicio+=1