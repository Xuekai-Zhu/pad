def solution():
    """Layla is feeding her pet fish. She has two Goldfish which each get one teaspoon of fish food. Her 3 Swordtails each get 2 teaspoons of food. Her 8 Guppies each eat half a teaspoon of food. How much food does she have to give to her fish in total?"""
    goldfish = 2
    swordtails = 3
    guppies = 8
    goldfish_food = goldfish * 1
    swordtail_food = swordtails * 2
    guppy_food = guppies * 0.5
    total_food = goldfish_food + swordtail_food + guppy_food
    result = total_food
    return result

print(solution())