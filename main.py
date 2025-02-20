def verificar_aprovacao(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

def verificar_eligibilidade_voto(idade):
    if idade >= 16:
        return "Pode votar"
    else:
        return "Não pode votar"

def classificar_nota(nota):
    if 90 <= nota <= 100:
        return "Parabéns, você tirou A!"
    elif 80 <= nota < 90:
        return "Muito bem, você tirou B."
    elif 70 <= nota < 80:
        return "Bom trabalho, você tirou C."
    elif 60 <= nota < 70:
        return "Fique atento, você tirou D."
    else:
        return "Estude um pouco mais, você tirou F."

def somar_numeros(a, b):
    return a + b

def verificar_senha(senha):
    return senha == "Python123"

def contar_ate_10():
    i = 1
    while i <= 10:
        print(i)
        i += 1

def organizar_lista():
    numeros = [8, 3, 10, 1, 5]
    return sorted(numeros)

def acessar_registros_alunos():
    alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
    return alunos[0], alunos[-1]

def dobro(numero):
    return f"O dobro de {numero} é {numero * 2}"

def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras"


print(verificar_aprovacao(7))  
print(verificar_eligibilidade_voto(15))  
print(classificar_nota(85))  
print(somar_numeros(4, 6))  
print(verificar_senha("Python123"))  
contar_ate_10()  
print(organizar_lista())  
print(acessar_registros_alunos())  
print(dobro(5))  
print(contar_letras("Ana"))  
