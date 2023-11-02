def solution():
    robbie_weight = 100  # Robbie weighs 100 pounds
    patty_weight = robbie_weight * 4.5  # Patty was 4.5 times as heavy as Robbie
    patty_weight_after_workout = patty_weight - 235  # Patty has lost 235 pounds by working out
    weight_difference = patty_weight_after_workout - robbie_weight  # Calculate the weight difference between Patty and Robbie
    result = weight_difference
    return result

print(solution())