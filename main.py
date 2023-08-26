def bubble_sort(arrOfInt):
    for i in range(len(arrOfInt)):
        for j in range(0, len(arrOfInt) - i - 1):
            if arrOfInt[j] > arrOfInt[j + 1]:
                arrOfInt[j], arrOfInt[j + 1] = arrOfInt[j + 1], arrOfInt[j]


numbers = [10, 22, 15, 0, -10, -32, -54]
print(f"array before bubble sorting = {numbers}")
bubble_sort(numbers)
print(f"array after bubble sorting = {numbers}")
