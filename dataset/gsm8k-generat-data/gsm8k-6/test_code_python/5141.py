def solution():
    # Calculate the cost of the food items
    food_cost = 9 + 20*2 + 11  # cost of appetizer, two entrees and dessert

    # Calculate the tip amount
    tip = 0.3 * food_cost  # 30% tip

    # Calculate the total cost of the meal
    total_cost = food_cost + tip

    result = total_cost
    return result

print(solution())