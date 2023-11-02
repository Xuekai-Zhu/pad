def solution():
    """There are 50 goldfish in the pond. Each goldfish eats 1.5 ounces of food per day. 20% of the goldfish need to eat special food that costs $3 an ounce. How much does it cost to feed these fish?"""
    num_fish_special_food = 0.2 * 50
    special_food_cost = num_fish_special_food * 1.5 * 3
    result = special_food_cost
    return result

print(solution())