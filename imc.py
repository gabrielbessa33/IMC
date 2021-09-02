
peso = float(input("Informe seu peso: "))
altura= float(input("Informe sua altura: "))

def num_neg(): 
    if peso or altura < 0:
        print("NUMERO INCORRETO")
        print("APENAS NUMEROS POSITIVOS PODEM SER INSERIDOS")

def imc_c():
    imc = peso/(altura**2)

def cal_imc(peso_):
    imc = peso/(altura**2)
    print("Resultado do IMC é: ",round(imc, 2) , peso_)

def imc_peso():
    if imc <= 18.5:
        cal_imc("ABAIXO DO PESO")
    elif imc > 18.6 and imc<= 24.9:
        cal_imc("PESO NORMAL")
    elif imc > 25 and imc<= 29.9:
        cal_imc("ACIMA DO PESO")
    else:
        cal_imc("OBESIDADE")


imc = peso/(altura**2)


if peso or altura < 0:
    num_neg()

imc_peso()




   
    
