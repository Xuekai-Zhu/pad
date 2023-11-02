def solution():
    """A bottle of wine costs $20.00 today. When new tariffs are imposed in 2 months, the price of wine will increase by 25%. How much more expensive will 5 bottles of wine be in 2 months?"""
    price_per_bottle = 20.00
    tariff_increase = 0.25
    new_price_per_bottle = price_per_bottle + (price_per_bottle * tariff_increase)
    num_bottles = 5
    total_increase = (new_price_per_bottle - price_per_bottle) * num_bottles
    result = total_increase
    return result

print(solution())