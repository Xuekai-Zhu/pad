def solution():
    """Donald went to a computer store. He saw a 15% reduction in the price of the laptop he wants to buy. If the laptop originally costs $800, how much will he pay for the laptop?"""
    original_price = 800
    reduction_percent = 15
    reduction_amount = original_price * (reduction_percent / 100)
    final_price = original_price - reduction_amount
    result = final_price
    return result

print(solution())