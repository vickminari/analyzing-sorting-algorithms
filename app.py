from insertion import insertion_sort
from bubble import bubble_sort
from selection import selection_sort
from bucket import bucket_sort
from shell import shell_sort
import time

def read_file(file_name):   #alterar para ler um arquivo de numeros
    file_path = f'lists/{file_name}'
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()


def main():
    fileName = 'nomes1k.txt' #alterar para o arquivo desejado
    for i in range(5):
        arr = read_file(fileName)

        # insetion sort
        start_time = time.time()
        insertion_sort(arr)
        insertion_duration = time.time() - start_time
        # print(f"Insertion Sort took {insertion_duration:.6f} seconds")
        print(f"Insertion Sort took {(insertion_duration*1000):.6f} milliseconds")

        # bubble sort
        start_time = time.time()
        bubble_sort(arr)
        bubble_duration = time.time() - start_time
        # print(f"Bubble Sort took {bubble_duration:.6f} seconds")
        print(f"Bubble Sort took {(bubble_duration*1000):.6f} milliseconds")

        # selection sort
        start_time = time.time()
        selection_sort(arr)
        selection_duration = time.time() - start_time
        # print(f"Selection Sort took {selection_duration:.6f} seconds")
        print(f"Selection Sort took {(selection_duration*1000):.6f} milliseconds")
        
        # bucket sort
        start_time = time.time()
        bucket_sort(arr)
        bucket_duration = time.time() - start_time
        # print(f"Bucket Sort took {bucket_duration:.6f} seconds")
        print(f"Bucket Sort took {(bucket_duration*1000):.6f} milliseconds")

        # shell sort
        start_time = time.time()
        shell_sort(arr)
        shell_duration = time.time() - start_time
        # print(f"Shell Sort took {shell_duration:.6f} seconds")
        print(f"Shell Sort took {(shell_duration*1000):.6f} milliseconds")
        

if __name__ == "__main__":
    main()