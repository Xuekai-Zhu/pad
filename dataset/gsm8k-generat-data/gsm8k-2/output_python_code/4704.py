def solution():
    """Jackson had 20 kilograms of meat. He used 1/4 of the meat to make meatballs and used 3 kilograms of meat to make spring rolls. How many kilograms of meat are left?"""
    starting_meat = 20
    meatballs = starting_meat * (1/4)
    spring_rolls = 3
    remaining_meat = starting_meat - meatballs - spring_rolls
    result = remaining_meat
    return result

print(solution())