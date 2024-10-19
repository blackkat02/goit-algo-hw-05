def binary_search(arr, x):
    if x > arr[-1]:
        return "x > arr[max]"
    elif x < arr[0]:
        return "x < arr[min]"
    elif not any(arr):
        return "Список пустий"

    count = 0
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        count += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return count, mid

    # якщо елемент не знайдений, знаходимо позицію більшого елемента за заданий в пошуку
    if arr[mid - 1] < x < arr[mid]:
        return count, mid
    elif arr[mid] < x < arr[mid + 1]:
        return count, mid + 1
    elif arr[mid + 1] < x < arr[mid + 2]:
        return count, mid + 2


arr = [2.3, 3.8, 4.0, 10.01, 40.05, 45.6, 48.8, 51.1, 52.7, 53.7, 54.7]
x = 54.5
result = binary_search(arr, x)
print(result)
