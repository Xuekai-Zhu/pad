def solution():
    """Adam had a farm with animals. He had 12 cows and twice as many sheep. He decided to buy 3 pigs for every sheep he had. How many animals were on the farm after the transaction?"""
    # Define the initial number of cows and sheep
    cows = 12
    sheep = 2 * cows

    # Calculate the number of pigs based on the number of sheep
    pigs = 3 * sheep

    # Add the number of cows, sheep, and pigs to get the total number of animals
    total_animals = cows + sheep + pigs

    # return the result
    result = total_animals
    return result

print(solution())