list_of_numbers = [4,2,6,8,5,7]

for i in range(len(list_of_numbers)):
    for j in range(len(list_of_numbers) - 1):
        if list_of_numbers[j] > list_of_numbers[j+1]:
            list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
            print(list_of_numbers)