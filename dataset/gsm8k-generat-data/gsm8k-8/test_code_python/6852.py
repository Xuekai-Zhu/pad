def solution():
    # Calculate the discounted price of the $300 lens
    discount = 0.2
    discounted_price = 300 * (1 - discount)

    # Compare the prices and calculate the amount saved by buying the cheaper lens
    if discounted_price < 220:
        amount_saved = 300 - discounted_price
    else:
        amount_saved = 300 - 220
    
    result = amount_saved
    return result

print(solution())