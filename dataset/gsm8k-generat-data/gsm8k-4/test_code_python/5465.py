def solution():
    """Donald went to a computer store. He saw a 15% reduction in the price of the laptop he wants to buy. If the laptop originally costs $800, how much will he pay for the laptop?"""
    # Define the original price of the laptop
    original_price = 800

    # Calculate the reduction amount
    reduction = original_price * 0.15

    # Calculate the new price after reduction
    new_price = original_price - reduction

    # return the result
    result = new_price
    return result

print(solution())