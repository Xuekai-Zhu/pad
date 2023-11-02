def solution():
    """Teddy is a pillow-maker.  He uses 3 less than 5 pounds of fluffy foam material to make each pillow.  If Teddy has three tons of fluffy foam material, how many pillows can he make?"""
    # Define the amount of fluffy foam material needed per pillow
    FOAM_PER_PILLOW = 5 - 3 # 5 pounds minus 3 pounds

    # Define the total amount of fluffy foam material Teddy has
    TOTAL_FOAM = 3 * 2000 # 3 tons = 6000 pounds

    # Calculate the number of pillows Teddy can make
    num_pillows = TOTAL_FOAM // FOAM_PER_PILLOW

    # Display the number of pillows Teddy can make
    result = num_pillows
    return result

print(solution())