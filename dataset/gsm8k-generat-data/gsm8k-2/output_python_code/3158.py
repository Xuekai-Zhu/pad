def solution():
    """Layla is feeding her pet fish. She has two Goldfish which each get one teaspoon of fish food. Her 3 Swordtails each get 2 teaspoons of food. Her 8 Guppies each eat half a teaspoon of food. How much food does she have to give to her fish in total?"""
    goldfish_food = 2 * 1
    swordtails_food = 3 * 2
    guppies_food = 8 * 0.5
    total_food = goldfish_food + swordtails_food + guppies_food
    result = total_food
    return result

print(solution())