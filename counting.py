def counting_sort(arr):
    if len(arr) == 0:
        return arr

    # Determinar o menor e o maior valor
    min_value = min(arr)
    max_value = max(arr)
    range_of_elements = max_value - min_value + 1

    # Criar e preencher o array de contagem
    count = [0] * range_of_elements
    for num in arr:
        count[num - min_value] += 1

    # Somar acumulativamente no array de contagem
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Construir o array de saída
    output = [0] * len(arr)
    for num in reversed(arr):  # Reverso para garantir estabilidade
        count[num - min_value] -= 1
        output[count[num - min_value]] = num

    return output

