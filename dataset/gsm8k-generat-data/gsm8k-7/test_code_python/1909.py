def solution():
    num_kids = 40
    less_than_6min = 0.1 * num_kids
    less_than_8min = 3 * less_than_6min
    remaining_kids = num_kids - less_than_6min - less_than_8min
    more_than_14min = (1/6) * remaining_kids
    result = more_than_14min
    return result

print(solution())