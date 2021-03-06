# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

COLUNA_GENERO = 6
COLUNA_TIPO_USUARIO = 5
COLUNA_DURACAO_VIAGEM = 2
COLUNA_ESTACAO_INICIO = 3

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(20):
    print(data_list[i])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for line in data_list[:20]:
    print(line[COLUNA_GENERO])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data: list, index: int):
    """
    Retorna a coluna especificada por index (em data) em forma de lista
    Args:
        data: uma lista de outra lista de n valores
        index: um valor entre 0 e n-1
    Returns:
        uma lista
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for line in data:
        column_list.append(line[index])
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, COLUNA_GENERO)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornando. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornando."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
coluna_genero = column_to_list(data_list, COLUNA_GENERO)
male = len( [m for m in coluna_genero if m == 'Male' ] )
female = len( [m for m in coluna_genero if m == 'Female' ] )

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria Returnsr uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list: list):
    """
    Retorna uma lista (de dois valores) com a quantidade de registros de usuários masculinos e femininos
    Args:
        data_list: uma lista de valores de gêneros (Male, Female ou valores nulos)
    Returns:
        uma lista de dois valores [Quantidade de usuários masculinos, Quantidade de usuários Femininos]
    """
    male = len( [m for m in column_to_list(data_list, COLUNA_GENERO) if m == 'Male' ] )
    female = len( [m for m in column_to_list(data_list, COLUNA_GENERO) if m == 'Female' ] )
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornando. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornando."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list: list):
    """
    Retorna uma descrição do gênero mais frequente na lista fornecida
    Args:
        data_list: uma lista de dois valores contendo uma quantidade de gêneros masculinos e femininos [masculino, feminino]
    Returns:
        a string 'Masculino' se existirem mais gêneros masculinos que femininos
        a string 'Feminino' se existirem mais gêneros femininos que masculinos
        a string 'Igual' se as quantidades forem equivalentes
    """
    GENERO_MALE = 0
    GENERO_FEMALE = 1
    contagem_genero = count_gender(data_list)
    if contagem_genero[GENERO_MALE] > contagem_genero[GENERO_FEMALE]:
        return "Masculino"
    elif contagem_genero[GENERO_MALE] == contagem_genero[GENERO_FEMALE]:
        return "Igual"
    return "Feminino"


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, COLUNA_GENERO)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
def count_user_types(data_list):
    """
    Retorna a quantidade de ocorrências de cada tipo de usuários em data_list
    Args:
        data_list: uma lista de tipos de usuários contendo valores 'Subscriber' e 'Customer'
    Returns:
        uma lista de dois valores com as quantidades de usuários do tipo 'Subscriber' e 'Customer'
        [Quantidade de subscriber, Quantidade de Customer]
    """
    subscriber = len( [m for m in column_to_list(data_list, COLUNA_TIPO_USUARIO) if m == 'Subscriber' ] )
    customer = len( [m for m in column_to_list(data_list, COLUNA_TIPO_USUARIO) if m == 'Customer' ] )
    return [subscriber, customer]

user_type_list = column_to_list(data_list, COLUNA_TIPO_USUARIO)
types = ["Subscriber", "Customer"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo de usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque alguns registros de usuários não possuem o sexo definido, o valor para esse dado está em branco."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
def soma_total(lista: list):
    """
    Retorna a soma de todos os números fornecidos na lista
    Args:
        uma lista de valores numéricos
    Returns:
        a soma total dos valores da lista
    """
    total = 0
    for numero in lista:
        total+=numero
    return total

def calcula_mediana(valores: list):
    """
    Retorna a mediana dos valores fornecidos
    Args:
        uma lista de valores numéricos
    Returns:
        a mediana dos valores fornecidos na lista
    """
    valores = sorted( [v for v in valores] )
    tamanho_lista = len(valores)

    if tamanho_lista == 0:
        return 0

    if tamanho_lista%2 == 0:
        indice = int(tamanho_lista/2)
        return (valores[indice - 1] + valores[indice])/2
    else:
        return valores[int(tamanho_lista/2)]

trip_duration_list = column_to_list(data_list, COLUNA_DURACAO_VIAGEM)
trip_duration_list = [int(v) for v in trip_duration_list]
min_trip = sorted( [n for n in trip_duration_list] )[0]
max_trip = sorted( [n for n in trip_duration_list] , reverse=True)[0]
mean_trip = soma_total(trip_duration_list)/len(trip_duration_list)
median_trip = calcula_mediana(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------


input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations_list = column_to_list(data_list, COLUNA_ESTACAO_INICIO)
start_stations = set(start_stations_list)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------


input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#    """
#      Função de exemplo com anotações.
#      Args:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Returns:
#          Uma lista de valores x.
#
#    """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list: list):
    """
    Retorna os diferentes itens presentes em columns_list e as suas respectivas quantidades
    Args:
        column_list: uma lista de valores qualquer
    Returns:
        duas listas
        a primeira com os exclusivos e diferentes valores contidos em column_list
        a segunda com as quantidades de ocorrências de cada um desses valores respectivamente
    """
    item_types = list(set(column_list))
    count_items = []
    for i in item_types:
        count_items.append( len( [m for m in column_list if m == i ] ) )
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
