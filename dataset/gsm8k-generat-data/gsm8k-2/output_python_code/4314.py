def solution():
    """A watermelon weighs 23 pounds. If Farmer Kent sells his special watermelons for $2 a pound, how much money would he make for selling 18 watermelons of the same weight?"""
    watermelon_weight = 23
    price_per_pound = 2
    total_weight = watermelon_weight * 18
    total_price = total_weight * price_per_pound
    result = total_price
    return result

print(solution())