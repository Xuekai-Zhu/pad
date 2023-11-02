def solution():
    # Calculate the price of the bed
    bed_price = 75 * 10

    # Calculate the total cost before discount
    total_cost = bed_price + 75

    # Calculate the total cost after discount
    discount = 0.2 * total_cost
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())