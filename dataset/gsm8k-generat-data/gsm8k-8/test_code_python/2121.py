def solution():
    # Calculate the cost of a jar of almond butter
    almond_butter_cost = 3 * 3

    # Calculate the cost of using half a jar of peanut butter and almond butter
    peanut_butter_cost_per_batch = 3 * 0.5
    almond_butter_cost_per_batch = almond_butter_cost * 0.5

    # Calculate the difference in cost per batch
    difference_in_cost_per_batch = almond_butter_cost_per_batch - peanut_butter_cost_per_batch
    result = difference_in_cost_per_batch
    return result

print(solution())