def solution():
    # Calculate the prices of the three products
    smartphone_price = 300
    pc_price = smartphone_price + 500  # personal computer costs $500 more than smartphone
    tablet_price = smartphone_price + pc_price  # advanced tablet costs the sum of smartphone and personal computer prices
    total_price = smartphone_price + pc_price + tablet_price  # calculate total price

    result = total_price
    return result

print(solution())