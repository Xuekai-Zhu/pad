def solution():
    """A bag has seven apples, eight oranges, and 15 mangoes. Luisa takes out two apples from the bag, and takes out twice as many oranges as apples as she took from the bag. She then takes out 2/3 the number of mangoes from the bag. What is the remaining number of fruits in the bag?"""
    # Define the initial number of fruits
    apples = 7
    oranges = 8
    mangoes = 15

    # Take out 2 apples from the bag
    apples -= 2

    # Take out twice as many oranges as apples
    oranges_taken = 2 * 2  # Two apples taken out
    oranges -= oranges_taken

    # Take out 2/3 the number of mangoes from the bag
    mangoes_taken = int(2/3 * mangoes)
    mangoes -= mangoes_taken

    # Calculate the remaining number of fruits
    remaining_fruits = apples + oranges + mangoes

    # return the result
    result = remaining_fruits
    return result

print(solution())