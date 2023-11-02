def solution():
    """Following her doctor’s recommendation to up her daily water intake, Nancy now drinks the equivalent of 60% of her body weight in water. If Nancy’s daily water intake is 54 pounds, how much, in pounds, does she weigh?"""
    water_intake_percent = 0.6
    water_intake_pounds = 54
    body_weight_pounds = water_intake_pounds / water_intake_percent
    result = body_weight_pounds
    return result

print(solution())