def solution():
    rabbit_food_cost = 12  # The weekly cost of the rabbit food is $12
    total_weeks = 5 + 3  # Julia had the rabbit for 5 weeks and the parrot for 3 weeks
    total_cost = 30 * total_weeks  # The total cost for both animals is $30 per week

    # Calculate the amount spent on parrot food
    parrot_food_cost = total_cost - rabbit_food_cost * 5
    result = parrot_food_cost
    return result

print(solution())