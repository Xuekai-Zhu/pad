def solution():
    # Calculate the total amount of ant food required
    ants = 400
    food_per_ant = 2
    total_food = ants * food_per_ant

    # Calculate the total cost of ant food
    cost_per_ounce = 0.1
    total_cost = total_food * cost_per_ounce

    # Calculate the total amount of money Nikola earned
    leaves_per_job = 500
    leaves_raked = 6000
    jobs_completed = (leaves_raked // leaves_per_job) + 1
    total_earnings = (jobs_completed * 5) + (leaves_raked * 0.01)

    # Check if Nikola has enough money to buy the ant food
    if total_earnings >= total_cost:
        result = jobs_completed
    else:
        result = "Nikola does not have enough money to start his ant farm"

    return result

print(solution())