def solution():
    """Mark orders 100 chicken nuggets. A 20 box of chicken nuggets cost $4. How much did he pay for the chicken nuggets?"""
    # Calculate how many boxes of chicken nuggets he needs
    num_boxes = 100 // 20 + (1 if 100 % 20 != 0 else 0)

    # Calculate the total cost of the chicken nuggets
    total_cost = num_boxes * 4

    # Display the total cost
    result = total_cost
    return result

print(solution())