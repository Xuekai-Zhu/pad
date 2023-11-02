def solution():
    num_bread = 200

    # Calculate how many pieces of bread Lucca ate on the first day
    eaten_first_day = num_bread / 4

    # Calculate how many pieces of bread remained after the first day
    remaining_after_first_day = num_bread - eaten_first_day

    # Calculate how many pieces of bread Lucca ate on the second day
    eaten_second_day = (2/5) * remaining_after_first_day

    # Calculate how many pieces of bread remained after the second day
    remaining_after_second_day = remaining_after_first_day - eaten_second_day

    # Calculate how many pieces of bread Lucca ate on the third day
    eaten_third_day = remaining_after_second_day / 2

    # Calculate how many pieces of bread are remaining after the third day
    remaining_after_third_day = remaining_after_second_day - eaten_third_day
    result = remaining_after_third_day
    return result

print(solution())