def solution():
    
    # Define the initial prices of the pomegranates
    initial_price = 20 * 20

    # Calculate the discounted prices after the voucher discount
    discounted_price = initial_price - 2

    # Calculate the total cost after the voucher discount
    total_cost = 20 * discounted_price

    # Calculate the discounted price after the 10% discount
    discounted_price *= 0.9

    # Calculate the difference between the final prices paid
    difference = discounted_price - initial_price

    # return the result
    result = difference
    return result

print(solution())