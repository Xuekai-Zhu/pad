def solution():
    """Jackson had 20 kilograms of meat. He used 1/4 of the meat to make meatballs and used 3 kilograms of meat to make spring rolls. How many kilograms of meat are left?"""
    initial_amount = 20
    meatballs_amount = initial_amount * (1/4)
    spring_rolls_amount = 3
    remaining_amount = initial_amount - meatballs_amount - spring_rolls_amount
    result = remaining_amount
    return result

print(solution())