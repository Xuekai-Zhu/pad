def solution():
    # Define the initial number of apples, oranges, and mangoes
    apples = 7
    oranges = 8
    mangoes = 15

    # Luisa takes out two apples and twice as many oranges as apples
    apples -= 2
    oranges -= 2 * 2

    # Luisa takes out 2/3 of the remaining mangoes
    mangoes -= int(mangoes * (2/3))

    # Calculate the remaining number of fruits
    remaining_fruits = apples + oranges + mangoes
    result = remaining_fruits
    return result

print(solution())