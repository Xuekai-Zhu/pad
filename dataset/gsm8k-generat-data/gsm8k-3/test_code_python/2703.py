def solution():
    """There are 6 boxes of crayons that hold 8 orange crayons. There are 7 boxes of crayons that have 5 blue crayons. There is 1 box of 11 red crayons. How many crayons are there in total?"""
    # Define the number of orange crayons per box and the number of boxes
    ORANGE_PER_BOX = 8
    ORANGE_BOXES = 6

    # Define the number of blue crayons per box and the number of boxes
    BLUE_PER_BOX = 5
    BLUE_BOXES = 7

    # Define the number of red crayons in the box
    RED_PER_BOX = 11
    RED_BOXES = 1

    # Calculate the total number of crayons
    total_orange = ORANGE_PER_BOX * ORANGE_BOXES
    total_blue = BLUE_PER_BOX * BLUE_BOXES
    total_red = RED_PER_BOX * RED_BOXES
    total_crayons = total_orange + total_blue + total_red

    # Display the total number of crayons
    result = total_crayons
    return result

print(solution())