def solution():
    # Calculate the new prices after the 20% reduction
    new_shirt_price = 0.8 * 60  # 20% reduction on $60 shirt
    new_jacket_price = 0.8 * 90  # 20% reduction on $90 leather jacket

    # Calculate the total cost of purchasing 5 shirts and 10 leather jackets
    total_cost = (5 * new_shirt_price) + (10 * new_jacket_price)
    result = total_cost
    return result

print(solution())