def solution():
    num_pins = 10
    original_price = 20
    discount = 0.15  # 15% discount

    # Calculate the discounted price for one pin
    discounted_price = original_price - (original_price * discount)

    # Calculate the total cost of all pins
    total_cost = num_pins * discounted_price
    result = total_cost
    return result

print(solution())