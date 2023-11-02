def solution():
    """John cuts his grass to 2 inches.  It grows .5 inches per month. When it gets to 4 inches he cuts it back down to 2 inches. It cost $100 to get his grass cut. How much does he pay per year?"""
    # Define the growth rate of the grass
    GROWTH_RATE = 0.5

    # Define the cost to cut the grass
    CUTTING_COST = 100

    # Define the height of the grass after each cut
    HEIGHT_AFTER_CUT = 2

    # Calculate the number of cuts per year
    months_per_year = 12
    height_before_cut = 4
    cuts_per_year = height_before_cut / GROWTH_RATE / months_per_year + 1

    # Calculate the total cost per year
    total_cost = cuts_per_year * CUTTING_COST

    # Display the total cost per year
    result = total_cost
    return result

print(solution())