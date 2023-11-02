def solution():
    """Robbie weighs 100 pounds. Patty was 4.5 times as heavy as Robbie, but she has since lost 235 pounds by working out. How many more pounds does Patty weigh than Robbie now?"""
    # Define Robbie's weight
    robbie_weight = 100

    # Calculate Patty's initial weight
    patty_weight = robbie_weight * 4.5

    # Calculate Patty's current weight
    patty_weight_now = patty_weight - 235

    # Calculate the difference between Patty's current weight and Robbie's weight
    weight_difference = patty_weight_now - robbie_weight

    result = weight_difference
    return result

print(solution())