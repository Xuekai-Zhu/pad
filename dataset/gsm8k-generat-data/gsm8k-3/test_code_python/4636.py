def solution():
    """Randy had 32 biscuits. His father gave him 13 biscuits as a gift. His mother gave him 15 biscuits. Randy’s brother ate 20 of these biscuits. How many biscuits are Randy left with?"""
    # Define the initial number of biscuits
    initial_biscuits = 32

    # Define the number of biscuits given by Randy's father
    father_biscuits = 13

    # Define the number of biscuits given by Randy's mother
    mother_biscuits = 15

    # Define the number of biscuits eaten by Randy's brother
    brother_biscuits = 20

    # Calculate the number of biscuits left with Randy
    biscuits_left = initial_biscuits + father_biscuits + mother_biscuits - brother_biscuits

    # Display the number of biscuits left with Randy
    result = biscuits_left
    return result

print(solution())