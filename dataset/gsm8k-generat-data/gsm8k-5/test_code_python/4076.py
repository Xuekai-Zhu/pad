def solution():
    num_goldfish = 50
    food_per_goldfish = 1.5  # ounces of food per day
    num_special_fish = int(num_goldfish * 0.2)  # 20% of goldfish need special food
    special_food_cost = 3  # dollars per ounce

    # Calculate the total cost of feeding the special fish
    special_food_amount = num_special_fish * food_per_goldfish
    special_food_cost_total = special_food_amount * special_food_cost
    result = special_food_cost_total
    return result

print(solution())