def solution():
    """Morisette and Kael were asked to bring fruits. Morisette brought 5 apples and 8 oranges, while Kael brought twice the amount of apples and half the number of oranges than Morisette. How many fruits do they have in total?"""
    morisette_apples = 5
    morisette_oranges = 8
    kael_apples = 2 * morisette_apples
    kael_oranges = morisette_oranges / 2
    total_fruits = morisette_apples + morisette_oranges + kael_apples + kael_oranges
    result = total_fruits
    return result

print(solution())