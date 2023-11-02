def solution():
    """Tree Elementary School is raising money for a new playground. Mrs. Johnson’s class raised $2300, which is twice the amount that Mrs. Sutton’s class raised. Mrs. Sutton’s class raised 8 times less than Miss Rollin’s class.
    Miss Rollin’s class raised a third of the total amount raised by the school.
    How much money did the school raise for the playground if 2% will be deducted for administration fees?"""
    johnsons_class = 2300
    suttons_class = johnsons_class / 2
    rollins_class = suttons_class + (8 * suttons_class)
    total_amount = rollins_class / (1/3)
    admin_fees = total_amount * 0.02
    total_amount_after_fees = total_amount - admin_fees
    result = total_amount_after_fees
    return result

print(solution())