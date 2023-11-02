def solution():
    """A box has 2 dozen water bottles and half a dozen more apple bottles than water bottles. How many bottles are in the box?"""
    # Define the number of bottles in a dozen
    DOZEN = 12

    # Define the number of water bottles in the box
    water_bottles = 2 * DOZEN

    # Define the number of apple bottles in the box
    apple_bottles = water_bottles + 0.5 * DOZEN

    # Calculate the total number of bottles in the box
    total_bottles = water_bottles + apple_bottles

    # return the result
    result = total_bottles
    return result

print(solution())