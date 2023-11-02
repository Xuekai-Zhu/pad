def solution():
    # Calculate the weekly cost of the parrot food
    total_weekly_cost = 30
    rabbit_weekly_cost = 12
    parrot_weekly_cost = total_weekly_cost - rabbit_weekly_cost
    # Calculate the total cost of the rabbit food
    rabbit_cost = rabbit_weekly_cost * 5

    # Calculate the total cost of the parrot food
    parrot_cost = parrot_weekly_cost * 3

    # Calculate the total spent on food for both animals
    total_food_cost = rabbit_cost + parrot_cost
    result = total_food_cost
    return result

print(solution())