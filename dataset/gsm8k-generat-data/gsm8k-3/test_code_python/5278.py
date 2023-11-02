def solution():
    """A box has 2 dozen water bottles and half a dozen more apple bottles than water bottles. How many bottles are in the box?"""
    # Define the number of bottles in a dozen
    DOZEN = 12

    # Define the number of water bottles and apple bottles
    water_bottles = 2 * DOZEN
    apple_bottles = water_bottles + (0.5 * DOZEN)

    # Calculate the total number of bottles in the box
    total_bottles = water_bottles + apple_bottles

    # Display the total number of bottles
    result = total_bottles
    return result

print(solution())