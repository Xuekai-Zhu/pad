def solution():
    # Calculate the total amount of food needed for 400 ants
    total_food = 400 * 2  # each ant needs 2 ounces of food

    # Calculate the cost of the total amount of food
    food_cost = total_food * 0.1  # every ounce of ant food costs $.1

    # Calculate the amount of money Nikola earned from raking leaves
    leaves_raked = 6000
    money_from_leaves = 5 + (leaves_raked * 0.01)  # he charges $5 to start a job and then charges by the leaf

    # Check if Nikola saved enough money for the ant food
    if money_from_leaves >= food_cost:
        # Calculate the number of jobs he completed
        jobs_completed = (money_from_leaves - food_cost) // 5  # he charges $5 to start a job
        result = jobs_completed
    else:
        result = "Nikola did not save enough money for the ant food."

    return result

print(solution())