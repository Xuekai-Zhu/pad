def solution():
    """Tree Elementary School is raising money for a new playground. Mrs. Johnson’s class raised $2300, which is twice the amount that Mrs. Sutton’s class raised. Mrs. Sutton’s class raised 8 times less than Miss Rollin’s class. Miss Rollin’s class raised a third of the total amount raised by the school. How much money did the school raise for the playground if 2% will be deducted for administration fees?"""
    johnson_class = 2300
    sutton_class = johnson_class / 2
    rollin_class = sutton_class * 8
    total_raised = rollin_class + sutton_class + johnson_class
    playground_fund = total_raised / 0.98
    result = playground_fund
    return result

print(solution())