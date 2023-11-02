def solution():
    # Calculate the total weight of the five girls
    girl_total_weight = 5 * 45

    # Calculate the total weight of the five boys
    boy_total_weight = 5 * 55

    # Calculate the total weight of all ten students
    total_weight = girl_total_weight + boy_total_weight

    # Calculate the average weight of all ten students
    average_weight = total_weight / 10
    result = average_weight
    return result

print(solution())