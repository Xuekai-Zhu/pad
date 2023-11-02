def solution():
    # Define Robbie's weight
    robbie_weight = 100

    # Calculate Patty's original weight
    patty_weight_original = 4.5 * robbie_weight

    # Calculate Patty's current weight after losing 235 pounds
    patty_weight_current = patty_weight_original - 235

    # Calculate the difference between Patty's current weight and Robbie's weight
    weight_difference = patty_weight_current - robbie_weight
    result = weight_difference
    return result

print(solution())