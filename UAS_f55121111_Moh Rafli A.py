import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"Iterasi {i+1}: {arr[:5]}")  # Menampilkan 5 iterasi pertama
    print(f"Iterasi terakhir: {arr[:5]}")  # Menampilkan 5 iterasi terakhir
    end_time = time.time()
    print(f"Waktu komputasi: {end_time - start_time} detik")
    return arr

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(f"Iterasi {i}: {arr[:5]}")  # Menampilkan 5 iterasi pertama
    print(f"Iterasi terakhir: {arr[:5]}")  # Menampilkan 5 iterasi terakhir
    end_time = time.time()
    print(f"Waktu komputasi: {end_time - start_time} detik")
    return arr

def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    print("Sebelum pengurutan:")
    print(arr)

    choice = input("Pilih metode pengurutan (bubble/insertion): ")

    if choice == "bubble":
        sorted_arr = bubble_sort(arr)
    elif choice == "insertion":
        sorted_arr = insertion_sort(arr)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    print("Setelah pengurutan:")
    print(sorted_arr)

if __name__ == "__main__":
    main()
