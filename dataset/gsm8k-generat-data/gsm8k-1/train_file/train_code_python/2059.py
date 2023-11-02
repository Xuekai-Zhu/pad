def solution():
    """Daisy’s milk cow provides 16 cups of milk per day. 75% of the milk is consumed by Daisy’s kids. Daisy uses 50% of the remaining milk to cook with. How much milk is left over?"""
    total_milk = 16
    kids_consumption = total_milk * 0.75
    remaining_milk = total_milk - kids_consumption
    cooking_milk = remaining_milk * 0.5
    leftover_milk = remaining_milk - cooking_milk
    result = leftover_milk

    return result

print(solution())