def solution():
    """Tree Elementary School is raising money for a new playground. Mrs. Johnson’s class raised $2300, which is twice the amount that Mrs. Sutton’s class raised. Mrs. Sutton’s class raised 8 times less than Miss Rollin’s class. Miss Rollin’s class raised a third of the total amount raised by the school. How much money did the school raise for the playground if 2% will be deducted for administration fees?"""
    # Calculate the amount raised by Miss Rollin's class
    rollins_class = 3 * 2300

    # Calculate the amount raised by Mrs. Sutton's class
    sutton_class = rollins_class / 8

    # Calculate the total amount raised by the school
    total_amount = 2300 + sutton_class + rollins_class

    # Calculate the amount to be deducted for administration fees
    admin_fees = 0.02 * total_amount

    # Calculate the net amount raised for the playground
    net_amount = total_amount - admin_fees

    result = net_amount
    return result

print(solution())