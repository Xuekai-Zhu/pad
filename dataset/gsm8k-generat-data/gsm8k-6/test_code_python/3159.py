def solution():
    # Calculate the total amount of fish food needed
    goldfish_food = 1 * 2  # two goldfish each get one teaspoon of food
    swordtails_food = 2 * 3  # three swordtails each get two teaspoons of food
    guppies_food = 0.5 * 8  # eight guppies each eat half a teaspoon of food
    total_food = goldfish_food + swordtails_food + guppies_food  # total amount of fish food needed
    result = total_food
    return result

print(solution())