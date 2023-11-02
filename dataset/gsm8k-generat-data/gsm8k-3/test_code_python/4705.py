def solution():
    """Jackson had 20 kilograms of meat. He used 1/4 of the meat to make meatballs and used 3 kilograms of meat to make spring rolls. How many kilograms of meat are left?"""
    # Define the initial amount of meat
    initial_meat = 20

    # Calculate the amount of meat used for meatballs
    meatballs = initial_meat / 4

    # Calculate the amount of meat used for spring rolls
    spring_rolls = 3

    # Calculate the amount of meat left
    remaining_meat = initial_meat - meatballs - spring_rolls

    # Display the amount of meat left
    result = remaining_meat
    return result

print(solution())