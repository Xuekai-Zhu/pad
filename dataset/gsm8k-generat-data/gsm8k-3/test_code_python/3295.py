def solution():
    """Karen and Donald and their 6 children are sharing a beach house with Tom and Eva and their 4 children. If there are 16 legs in the pool, how many people are not in the pool?"""
    # Define the number of legs for each person
    KAREN_LEGS = 2
    DONALD_LEGS= 2
    CHILD_LEGS = 2

    # Define the number of people in each family
    KAREN_FAMILY = 8
    TOM_FAMILY = 6

    # Calculate the number of legs in each family
    karen_legs = KAREN_LEGS * KAREN_FAMILY
    donald_legs = DONALD_LEGS * KAREN_FAMILY
    child_legs = CHILD_LEGS * (KAREN_FAMILY + TOM_FAMILY)

    # Calculate the total number of legs
    total_legs = karen_legs + donald_legs + child_legs

    # Calculate the number of people not in the pool
    people_outside = (KAREN_FAMILY + TOM_FAMILY) - (total_legs - 16)//2

    # Display the number of people not in the pool
    result = people_outside
    return result

print(solution())