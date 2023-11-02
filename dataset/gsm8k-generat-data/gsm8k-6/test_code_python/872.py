def solution():
    # Calculate the amount spent by John on pins after the discount
    original_price = 20  # original price of each pin
    discount = 0.15  # discount percentage
    discounted_price = original_price - (original_price * discount)  # price of each pin after the discount
    total_cost = discounted_price * 10  # total cost of 10 pins
    result = total_cost
    return result

print(solution())