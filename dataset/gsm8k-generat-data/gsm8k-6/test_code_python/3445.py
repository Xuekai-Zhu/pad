def solution():
    # Calculate the cost of buying individual food items
    cost_burger = 5
    cost_fries = 3
    cost_drink = 3
    cost_kid_burger = 3
    cost_kid_fries = 2
    cost_kid_drink = 2
    
    total_cost_individual = (cost_burger + cost_fries + cost_drink) * 2 + \
                            (cost_burger + cost_fries + cost_drink + cost_kid_burger + cost_kid_fries + cost_kid_drink) * 2

    # Calculate the cost of buying meal deals
    cost_burger_meal = 9.5
    cost_kid_meal = 5

    total_cost_meal_deals = (cost_burger_meal + cost_kid_meal) * 2 + \
                            (cost_burger_meal * 2)

    # Calculate the savings
    savings = total_cost_individual - total_cost_meal_deals
    
    result = savings
    return result

print(solution())