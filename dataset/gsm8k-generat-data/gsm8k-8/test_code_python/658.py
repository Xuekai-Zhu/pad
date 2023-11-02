def solution():
    # Calculate the discounted price for the first store
    price1 = 950 * (1 - 0.06)

    # Calculate the discounted price for the second store
    price2 = 920 * (1 - 0.05)
    
    # Calculate the difference in price
    difference = price1 - price2
    result = difference
    return result

print(solution())