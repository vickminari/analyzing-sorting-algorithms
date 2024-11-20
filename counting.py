def counting_sort(arr, char_index):
    """Ordena uma lista de strings com base em um caractere específico (char_index) usando Counting Sort."""
    n = len(arr)
    if n <= 1:
        return arr

    # Determinar o intervalo de caracteres ASCII (considerando strings de tamanho variável)
    max_char = 256  # Máximo para valores ASCII
    count = [0] * max_char

    # Passo 1: Contar ocorrências do caractere na posição char_index
    for string in arr:
        char = string[char_index] if char_index < len(string) else "\0"  # '\0' representa um "fim de string"
        count[ord(char)] += 1

    # Passo 2: Soma acumulativa
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Passo 3: Construir o array de saída
    output = ["" for _ in range(n)]
    for string in reversed(arr):  # Reverso para garantir estabilidade
        char = string[char_index] if char_index < len(string) else "\0"
        count[ord(char)] -= 1
        output[count[ord(char)]] = string

    return output


def radix_sort_strings(arr):
    """Ordena uma lista de strings usando Counting Sort em cada posição (Radix Sort)."""
    if len(arr) == 0:
        return arr

    # Determinar o tamanho da maior string
    max_len = max(len(string) for string in arr)

    # Ordenar da posição menos significativa (última) para a mais significativa (primeira)
    for char_index in reversed(range(max_len)):
        arr = counting_sort(arr, char_index)

    return arr
