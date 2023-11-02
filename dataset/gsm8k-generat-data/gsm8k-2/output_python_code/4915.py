def solution():
    """A bag has seven apples, eight oranges, and 15 mangoes. Luisa takes out two apples from the bag, and takes out twice as many oranges as apples as she took from the bag. She then takes out 2/3 the number of mangoes from the bag. What is the remaining number of fruits in the bag?"""
    apples = 7 - 2
    oranges = 8 - 2*2
    mangoes = 15 - int(2/3 * 15)
    total_fruits = apples + oranges + mangoes
    result = total_fruits
    return result

print(solution())