def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def bucket_sort(names):
    if len(names) == 0:
        return names

    # Passo 1: Criar os baldes baseados na primeira letra (A-Z)
    buckets = {chr(i): [] for i in range(ord('A'), ord('Z') + 1)}

    for name in names:
        first_letter = name[0]  # Considera a primeira letra (case insensitive)
        if first_letter in buckets:
            buckets[first_letter].append(name)

    # Passo 2: Ordenar os baldes usando Quick Sort
    for key in buckets:
        buckets[key] = quick_sort(buckets[key])

    # Passo 3: Concatenar os baldes
    sorted_names = []
    for key in sorted(buckets.keys()):  # Garantir a ordem alfabética dos baldes
        sorted_names.extend(buckets[key])

    return sorted_names
