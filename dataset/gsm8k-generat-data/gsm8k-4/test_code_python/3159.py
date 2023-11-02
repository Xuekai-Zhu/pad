def solution():
    """Layla is feeding her pet fish. She has two Goldfish which each get one teaspoon of fish food. Her 3 Swordtails each get 2 teaspoons of food. Her 8 Guppies each eat half a teaspoon of food. How much food does she have to give to her fish in total?"""
    # Define the amount of food needed for each type of fish
    goldfish_food = 2 * 1
    swordtail_food = 3 * 2
    guppy_food = 8 * 0.5

    # Calculate the total amount of food needed
    total_food = goldfish_food + swordtail_food + guppy_food

    # return the result
    result = total_food
    return result

print(solution())