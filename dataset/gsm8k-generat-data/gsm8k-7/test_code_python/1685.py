def solution():
    cost_of_burger_meal = 6.0
    cost_of_upsized_fries_and_drinks = 1.0
    num_days = 5

    # Calculate the total cost of all the burger meals
    total_cost_of_burger_meals = cost_of_burger_meal * num_days

    # Calculate the total cost of all the upsized fries and drinks
    total_cost_of_upsized_fries_and_drinks = cost_of_upsized_fries_and_drinks * num_days

    # Calculate the total cost of all the lunches
    total_cost = total_cost_of_burger_meals + total_cost_of_upsized_fries_and_drinks
    result = total_cost
    return result

print(solution())