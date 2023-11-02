def solution():
    """A watermelon weighs 23 pounds. If Farmer Kent sells his special watermelons for $2 a pound, how much money would he make for selling 18 watermelons of the same weight?"""
    weight_per_watermelon = 23
    price_per_pound = 2
    num_watermelons = 18
    total_weight = weight_per_watermelon * num_watermelons
    total_income = total_weight * price_per_pound
    result = total_income
    return result

print(solution())