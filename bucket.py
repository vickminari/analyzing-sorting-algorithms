def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Determine minimum and maximum values
    min_value = min(arr)
    max_value = max(arr)

    # Initialize buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for i in range(len(arr)):
        index = int((arr[i] - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(arr[i])

    # Sort each bucket and concatenate the result
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(quick_sort(bucket))

    return sorted_array

# # Example usage
# if __name__ == "__main__":
#     arr = [42, 32, 33, 52, 37, 47, 51]
#     print("Original array:", arr)
#     sorted_arr = bucket_sort(arr)
#     print("Sorted array:", sorted_arr)