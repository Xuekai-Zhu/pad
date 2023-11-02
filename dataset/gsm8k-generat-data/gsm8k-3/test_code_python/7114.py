def solution():
    """John buys 3 barbells and gives $850 and gets $40 in change.  How much did each barbell cost?"""
    # Calculate the total amount John paid
    total_paid = 850 - 40

    # Divide the total paid by the number of barbells to get the cost per barbell
    cost_per_barbell = total_paid / 3

    # Display the cost per barbell
    result = cost_per_barbell
    return result

print(solution())