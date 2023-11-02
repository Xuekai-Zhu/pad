def solution():
    total_apples = 200
    day_1 = total_apples * (1/5)
    day_2 = day_1 * 2
    day_3 = day_1 + 20

    # Calculate the total number of apples picked
    total_picked = day_1 + day_2 + day_3

    # Calculate the total number of apples remaining in the tree
    total_remaining = total_apples - total_picked
    result = total_remaining
    return result

print(solution())