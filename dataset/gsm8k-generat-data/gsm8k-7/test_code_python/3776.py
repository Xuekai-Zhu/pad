def solution():
    rabbit_weekly_cost = 12
    total_weekly_cost = 30
    rabbit_weeks = 5
    parrot_weeks = 3

    # Calculate the total cost for the rabbit's food
    rabbit_food_cost = rabbit_weekly_cost * rabbit_weeks

    # Calculate the total cost for both animals' food
    total_food_cost = total_weekly_cost * (rabbit_weeks + parrot_weeks)

    # Calculate the amount spent on the parrot's food
    parrot_food_cost = total_food_cost - rabbit_food_cost

    # Calculate the total amount spent on food for both animals
    total_spent = rabbit_food_cost + parrot_food_cost
    result = total_spent
    return result

print(solution())