def solution():
    """Ishmael, Ponce, and Jalen measured their weight and realized Ishmael was 20 pounds heavier than Ponce and that Ponce was 10 pounds lighter than Jalen. If Jalen weighed 160 pounds, calculate the average weight of the three?"""
    # Define Jalen's weight
    jalen_weight = 160

    # Calculate Ponce's weight
    ponce_weight = jalen_weight - 10

    # Calculate Ishmael's weight
    ishmael_weight = ponce_weight + 20

    # Calculate the sum of their weights
    total_weight = jalen_weight + ponce_weight + ishmael_weight

    # Calculate the average weight
    average_weight = total_weight / 3

    # Display the average weight
    result = average_weight
    return result

print(solution())