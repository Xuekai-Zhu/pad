def solution():
    jalen_weight = 160
    ponce_weight = jalen_weight - 10
    ishmael_weight = ponce_weight + 20

    # Calculate the total weight of the three
    total_weight = jalen_weight + ponce_weight + ishmael_weight

    # Calculate the average weight of the three
    average_weight = total_weight / 3
    result = average_weight
    return result

print(solution())