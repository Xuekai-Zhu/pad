def solution():
    """A crayon factory makes 4 colors of crayons. They put 2 of each color crayon in each box. The factory produces enough crayons to fill 5 boxes per hour. How many crayons does the factory produce in 4 hours?"""
    # Define the number of colors
    NUM_COLORS = 4

    # Define the number of crayons per color
    CRAYONS_PER_COLOR = 2

    # Define the number of boxes produced per hour
    BOXES_PER_HOUR = 5

    # Calculate the number of crayons produced per hour
    CRAYONS_PER_HOUR = NUM_COLORS * CRAYONS_PER_COLOR * BOXES_PER_HOUR

    # Calculate the total number of crayons produced in 4 hours
    TOTAL_CRAYONS = CRAYONS_PER_HOUR * 4

    # Display the total number of crayons produced
    result = TOTAL_CRAYONS
    return result

print(solution())