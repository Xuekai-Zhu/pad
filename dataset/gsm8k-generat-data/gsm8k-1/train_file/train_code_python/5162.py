def solution():
    """Rollo has 3 guinea pigs, the first guinea pig eats 2 cups of food, the second guinea pig eats twice as much as the first one, and the third guinea pig eats 3 cups more than the second one. How many cups of food does Rollo need to feed all his Guinea pigs?"""
    pig1_food = 2
    pig2_food = pig1_food * 2
    pig3_food = pig2_food + 3
    total_food = pig1_food + pig2_food + pig3_food
    result = total_food
    return result

print(solution())