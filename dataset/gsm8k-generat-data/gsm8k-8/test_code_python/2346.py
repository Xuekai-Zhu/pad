def solution():
    # Calculate the value of the old stereo after the trade-in
    trade_in_value = 0.8 * 250

    # Calculate the cost of the new stereo after the discount
    discounted_price = 0.75 * 600

    # Calculate the total amount paid out of pocket
    out_of_pocket = discounted_price - trade_in_value

    result = out_of_pocket
    return result

print(solution())