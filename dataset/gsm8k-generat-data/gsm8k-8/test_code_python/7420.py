def solution():
    # Calculate the total amount of ant food needed in ounces
    total_ant_food = 400 * 2

    # Calculate the total cost of ant food needed
    ant_food_cost = total_ant_food * 0.1

    # Calculate the total amount Nikola earned from leaf-raking
    total_earnings = (6000 * 0.01) + 5

    # Calculate the number of jobs Nikola completed
    num_jobs = (ant_food_cost - total_earnings) / 5

    # Round the result to the nearest whole number
    result = round(num_jobs)
    return result

print(solution())