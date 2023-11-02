def solution():
    """A bag has seven apples, eight oranges, and 15 mangoes. Luisa takes out two apples from the bag, and takes out twice as many oranges as apples as she took from the bag. She then takes out 2/3 the number of mangoes from the bag. What is the remaining number of fruits in the bag?"""
    # Define the starting number of fruits
    apples = 7
    oranges = 8
    mangoes = 15

    # Remove two apples from the bag
    apples -= 2

    # Remove twice as many oranges as apples
    oranges_removed = 2 * 2  # Luisa removes 2 apples
    oranges -= oranges_removed

    # Remove 2/3 of the mangoes from the bag
    mangoes_removed = int(mangoes * (2/3))
    mangoes -= mangoes_removed

    # Calculate the total number of fruits remaining in the bag
    total_fruits = apples + oranges + mangoes

    # Display the total number of fruits remaining in the bag
    result = total_fruits
    return result

print(solution())