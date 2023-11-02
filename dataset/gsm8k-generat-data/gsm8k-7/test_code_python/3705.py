def solution():
    num_girls = 5
    girls_weight = 45

    num_boys = 5
    boys_weight = 55

    # Calculate the total weight of all girls
    total_girls_weight = num_girls * girls_weight

    # Calculate the total weight of all boys
    total_boys_weight = num_boys * boys_weight

    # Calculate the total weight of all students
    total_weight = total_girls_weight + total_boys_weight

    # Calculate the average weight of all students
    average_weight = total_weight / (num_girls + num_boys)
    result = average_weight
    return result

print(solution())