def solution():
    num_peas = 35
    extra_peas = 15

    # Calculate the total number of cans of peas without the extra 15
    total_peas = num_peas - extra_peas

    # Calculate twice the number of cans of corn
    twice_corn = total_peas * 2

    # Calculate the number of cans of corn that Beth bought
    num_corn = (twice_corn - num_peas) / -1
    result = num_corn
    return result

print(solution())