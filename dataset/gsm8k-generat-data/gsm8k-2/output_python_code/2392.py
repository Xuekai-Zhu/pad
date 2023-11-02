def solution():
    """Robbie weighs 100 pounds. Patty was 4.5 times as heavy as Robbie, but she has since lost 235 pounds by working out. How many more pounds does Patty weigh than Robbie now?"""
    robbie_weight = 100
    patty_weight = robbie_weight * 4.5
    patty_weight_after_workout = patty_weight - 235
    weight_difference = patty_weight_after_workout - robbie_weight
    result = weight_difference
    return result

print(solution())