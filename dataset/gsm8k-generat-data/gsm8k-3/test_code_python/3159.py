def solution():
    """Layla is feeding her pet fish. She has two Goldfish which each get one teaspoon of fish food. Her 3 Swordtails each get 2 teaspoons of food. Her 8 Guppies each eat half a teaspoon of food. How much food does she have to give to her fish in total?"""
    # Define the amount of food for each type of fish
    GOLDFISH_FOOD = 1
    SWORDTAIL_FOOD = 2
    GUPPY_FOOD = 0.5

    # Define the number of each type of fish
    goldfish_num = 2
    swordtail_num = 3
    guppy_num = 8

    # Calculate the total amount of food needed
    total_food = (goldfish_num * GOLDFISH_FOOD) + (swordtail_num * SWORDTAIL_FOOD) + (guppy_num * GUPPY_FOOD)

    # Display the total amount of food needed
    result = total_food
    return result

print(solution())