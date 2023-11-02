def solution():
    """A bottle of wine costs $20.00 today. When new tariffs are imposed in 2 months, the price of wine will increase by 25%. How much more expensive will 5 bottles of wine be in 2 months?"""
    current_price = 20.00
    price_increase = 0.25
    new_price = current_price + (current_price * price_increase)
    num_bottles = 5
    current_total_price = current_price * num_bottles
    new_total_price = new_price * num_bottles
    price_difference = new_total_price - current_total_price
    result = price_difference
    return result

print(solution())