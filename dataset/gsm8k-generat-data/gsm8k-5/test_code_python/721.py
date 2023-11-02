def solution():
    smartphone_price = 300  # The price of a smartphone is $300
    pc_price = smartphone_price + 500  # The price of a personal computer is $500 more than a smartphone
    tablet_price = smartphone_price + pc_price  # The price of an advanced tablet is the sum of a smartphone and a personal computer

    # Calculate the total cost of buying one of each product
    total_cost = smartphone_price + pc_price + tablet_price
    result = total_cost
    return result

print(solution())