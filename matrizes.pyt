def ler_matrizes_arquivo(matrizes):
    matriz_a = []
    matriz_b = []
    matriz_atual = matriz_a

    with open(matrizes, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith("#"):
                if not linha:
                    matriz_atual = matriz_b
                continue
            matriz_atual.append([int(x) for x in linha.split()])

    return matriz_a, matriz_b

def eh_quadrada(matriz):
    return all(len(linha) == len(matriz) for linha in matriz)

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def multiplicar_matrizes(m1, m2):
    n = len(m1)
    resultado = [[0] * n for _ in range(n)]
    passos = []

    for i in range(n):
        for j in range(n):
            soma_temp = 0
            calculo = []
            for k in range(n):
                mult = multiplicacao(m1[i][k], m2[k][j])
                soma_temp = soma(soma_temp, mult)
                calculo.append(f"{m1[i][k]}*{m2[k][j]}")
            resultado[i][j] = soma_temp
            passos.append(f"C[{i+1},{j+1}] = {' + '.join(calculo)} = {resultado[i][j]}")
    return resultado, passos

def mostrar_matriz(m, nome="Matriz"):
    print(f"{nome}:")
    for linha in m:
        print(" ".join(f"{x:4}" for x in linha))
    print()

# --- PROGRAMA PRINCIPAL ---
arquivo = "matrizes.txt"
A, B = ler_matrizes_arquivo(arquivo)

# Verifica se são quadradas
if not eh_quadrada(A) or not eh_quadrada(B):
    print("Erro: Uma das matrizes não é quadrada.")
else:
    print("Matrizes carregadas com sucesso.\n")
    mostrar_matriz(A, "Matriz A")
    mostrar_matriz(B, "Matriz B")

    # Multiplicação
    C, passos = multiplicar_matrizes(A, B)

    print("Passo a passo da multiplicação:")
    for p in passos:
        print(p)
    print()
    mostrar_matriz(C, "Matriz Resultado (C = A x B)")
