def solution():
    """Randy had 32 biscuits. His father gave him 13 biscuits as a gift. His mother gave him 15 biscuits. Randy’s brother ate 20 of these biscuits. How many biscuits are Randy left with?"""
    # Define the initial number of biscuits
    biscuits = 32

    # Add the biscuits given by Randy's father and mother
    biscuits += 13 + 15

    # Subtract the biscuits eaten by Randy's brother
    biscuits -= 20

    # return the number of biscuits Randy is left with
    result = biscuits
    return result

print(solution())