def solution():
    bed_frame_price = 75  # The bed frame costs $75
    bed_price = 10 * bed_frame_price  # The bed costs 10 times the price of the bed frame
    total_price = bed_frame_price + bed_price  # The total price is the sum of the bed and bed frame prices
    discount = 0.2  # The discount is 20%

    # Calculate the discounted price
    discounted_price = total_price * (1 - discount)

    result = discounted_price
    return result

print(solution())