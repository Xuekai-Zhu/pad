def solution():
    spool_length = 15
    wick_length_1 = 6
    wick_length_2 = 12
    number_of_1 = spool_length / wick_length_1
    number_of_2 = spool_length / wick_length_2
    total_wicks = number_of_1 + number_of_2
    result = total_wicks
    return result

print(solution())