def solution():
    """An auto shop has a part that Clark needs for $80. Clark buys 7 of them and got a discount. If Clark only had to pay $439, how much was the discount?"""
    # Define the cost of each part and the number of parts bought
    part_cost = 80
    num_parts = 7

    # Calculate the total cost before the discount
    total_cost_before_discount = part_cost * num_parts

    # Calculate the discount
    discount = total_cost_before_discount - 439

    # return the result
    result = discount
    return result

print(solution())