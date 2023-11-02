def solution():
    # Find how many dandelions George picked
    george_picked = 1/3 * 36

    # Find the total number of dandelions before they picked more
    total_before = 36 + george_picked

    # Find the total number of dandelions after they picked more
    total_after = total_before + 10 + 10

    # Find the average number of dandelions they picked
    average_picked = total_after / 2

    result = average_picked
    return result

print(solution())