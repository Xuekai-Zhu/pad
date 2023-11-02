def solution():
    smartphone_price = 300
    pc_price = smartphone_price + 500
    tablet_price = smartphone_price + pc_price

    # Calculate the total cost of all three products
    total_cost = smartphone_price + pc_price + tablet_price
    result = total_cost
    return result

print(solution())