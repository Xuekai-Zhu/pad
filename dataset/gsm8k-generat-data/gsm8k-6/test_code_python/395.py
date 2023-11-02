def solution():
    # Calculate the number of elephants that left the park during the 4-hour period
    elephants_left = 2,880 * 4

    # Calculate the total number of elephants in the park after the exodus
    remaining_elephants = 30,000 - elephants_left

    # Calculate the rate at which new elephants entered the park over the 7-hour period
    entry_rate = (28,980 - remaining_elephants) / 7

    result = entry_rate
    return result

print(solution())