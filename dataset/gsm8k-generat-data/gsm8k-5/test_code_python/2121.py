def solution():
    peanut_butter_cost = 3  # A jar of peanut butter costs $3
    almond_butter_cost = 3 * 3  # A jar of almond butter costs three times the amount of peanut butter

    # Calculate the cost per batch of peanut butter cookies
    peanut_butter_per_batch = peanut_butter_cost / 2

    # Calculate the cost per batch of almond butter cookies
    almond_butter_per_batch = almond_butter_cost / 2

    # Calculate the difference in cost per batch between the two types of cookies
    cost_difference = almond_butter_per_batch - peanut_butter_per_batch
    result = cost_difference
    return result

print(solution())