def solution():
    """If there are four times as many red crayons as blue crayons in a box, and there are 3 blue crayons.  How many crayons total are in the box?"""
    # Define the number of blue crayons in the box
    blue_crayons = 3

    # Calculate the number of red crayons in the box
    red_crayons = blue_crayons * 4

    # Calculate the total number of crayons in the box
    total_crayons = blue_crayons + red_crayons

    # Display the total number of crayons in the box
    result = total_crayons
    return result

print(solution())