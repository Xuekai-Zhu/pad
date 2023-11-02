def solution():
    num_sandwiches = 12
    first_day = num_sandwiches / 2
    second_day = first_day - 2
    total_sandwiches_left = num_sandwiches - (first_day + second_day)
    result = total_sandwiches_left
    return result

print(solution())