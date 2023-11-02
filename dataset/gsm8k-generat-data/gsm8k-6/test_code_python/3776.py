def solution():
    rabbit_weekly_cost = 12  # weekly cost of rabbit food
    parrot_weekly_cost = (30 - rabbit_weekly_cost) / 2  # weekly cost of parrot food
    total_spent_on_rabbit_food = 5 * rabbit_weekly_cost  # total spent on rabbit food
    total_spent_on_parrot_food = 3 * parrot_weekly_cost  # total spent on parrot food
    total_spent_on_animal_food = total_spent_on_rabbit_food + total_spent_on_parrot_food
    result = total_spent_on_animal_food
    return result

print(solution())