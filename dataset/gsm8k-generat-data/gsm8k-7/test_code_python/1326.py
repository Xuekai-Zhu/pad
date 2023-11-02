def solution():
    num_tires = 4
    sale_price = 75
    total_saved = 36

    # Calculate the total cost of all tires at the sale price
    total_cost = num_tires * sale_price

    # Calculate the original cost of each tire before the sale
    original_price = (total_cost + total_saved) / num_tires
    result = original_price
    return result

print(solution())