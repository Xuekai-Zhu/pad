def solution():
    """James needs 200 blueberries to make a pint of blueberry jam and then a quart of blueberry jam to make a blueberry pie. If there are two pints per quart, how many blueberries does James need to pick to make 6 pies?"""
    # Define the number of blueberries needed to make a pint of blueberry jam and a quart of blueberry jam
    BLUEBERRIES_PER_PINT = 200
    BLUEBERRIES_PER_QUART = BLUEBERRIES_PER_PINT * 2

    # Define the number of pies James wants to make
    NUM_PIES = 6

    # Calculate the total number of blueberries needed to make the pies
    total_blueberries = NUM_PIES * BLUEBERRIES_PER_QUART

    # Display the total number of blueberries needed
    result = total_blueberries
    return result

print(solution())