def solution():
    # Calculate the number of apples picked on the first day
    apples_picked_first = 1/5 * 200

    # Calculate the number of apples picked on the second day
    apples_picked_second = 2 * apples_picked_first

    # Calculate the number of apples picked on the third day
    apples_picked_third = apples_picked_first + 20

    # Calculate the total number of apples picked
    total_apples_picked = apples_picked_first + apples_picked_second + apples_picked_third

    # Calculate the remaining number of apples
    remaining_apples = 200 - total_apples_picked
    result = remaining_apples
    return result

print(solution())