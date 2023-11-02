def solution():
    num_knives = 9  # Otto has 9 knives that need to be sharpened
    cost = 0

    # Calculate the cost for the first knife
    cost += 5

    # Calculate the cost for the next 3 knives
    if num_knives > 1:
        cost += 4 * min(num_knives-1, 3)
        num_knives -= 4

    # Calculate the cost for any additional knives beyond the first 4
    if num_knives > 0:
        cost += 3 * num_knives

    result = cost
    return result

print(solution())