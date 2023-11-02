def solution():
    """Mark orders 100 chicken nuggets. A 20 box of chicken nuggets cost $4. How much did he pay for the chicken nuggets?"""
    # Define the number of chicken nuggets and the price per box
    nuggets = 100
    price_per_box = 4

    # Calculate the total number of boxes required
    boxes = nuggets // 20
    if nuggets % 20 != 0:
        boxes += 1

    # Calculate the total cost of the chicken nuggets
    total_cost = boxes * price_per_box

    # Return the result
    result = total_cost
    return result

print(solution())