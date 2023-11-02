def solution():
    peanut_butter_cost = 3
    almond_butter_cost = peanut_butter_cost * 3
    almond_butter_needed = 0.5

    # Calculate the cost per batch of peanut butter cookies
    peanut_butter_cost_per_batch = peanut_butter_cost / 2

    # Calculate the cost per batch of almond butter cookies
    almond_butter_cost_per_batch = almond_butter_cost * almond_butter_needed / 2

    # Calculate how much more the almond butter cookies cost per batch
    extra_cost_per_batch = almond_butter_cost_per_batch - peanut_butter_cost_per_batch
    result = extra_cost_per_batch
    return result

print(solution())