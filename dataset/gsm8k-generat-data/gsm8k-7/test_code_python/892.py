def solution():
    part_price = 80
    num_parts = 7
    total_cost = 439

    # Calculate the cost of all parts without discount
    total_without_discount = part_price * num_parts

    # Calculate the discount amount
    discount = total_without_discount - total_cost
    result = discount
    return result

print(solution())