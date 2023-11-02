def solution():
    # Define Jalen's weight
    jalen_weight = 160

    # Calculate Ponce's weight
    ponce_weight = jalen_weight - 10

    # Calculate Ishmael's weight
    ishmael_weight = ponce_weight + 20

    # Calculate the average weight
    average_weight = (jalen_weight + ponce_weight + ishmael_weight) / 3
    result = average_weight
    return result

print(solution())