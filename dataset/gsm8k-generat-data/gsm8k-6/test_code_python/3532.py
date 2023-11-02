def solution():
    # Calculate the total number of portions from the sandwiches
    total_portions = 20 * 2 * 2  # each sandwich is cut in half twice

    # Calculate the number of people that can be fed
    num_people = total_portions // 8  # each person is given 8 portions
    result = num_people
    return result

print(solution())