def solution():
    # Calculate the total daily food needed for all the fish
    total_food_needed = 50 * 1.5  # each goldfish eats 1.5 ounces of food per day

    # Calculate the number of goldfish that need special food
    fish_need_special_food = 0.2 * 50  # 20% of the goldfish need special food

    # Calculate the cost to feed the fish that need special food
    special_food_cost = fish_need_special_food * 1.5 * 3  # $3 an ounce for special food, 1.5 ounces needed per fish

    result = special_food_cost
    return result

print(solution())