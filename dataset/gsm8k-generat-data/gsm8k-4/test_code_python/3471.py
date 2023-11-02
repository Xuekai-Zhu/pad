def solution():
    """Teddy is a pillow-maker.  He uses 3 less than 5 pounds of fluffy foam material to make each pillow.  If Teddy has three tons of fluffy foam material, how many pillows can he make?"""
    # Define the amount of foam material Teddy uses per pillow
    foam_per_pillow = 5 - 3  # Teddy uses 2 pounds of foam per pillow

    # Define the total amount of foam material Teddy has, in pounds
    total_foam = 3 * 2000  # Teddy has 3 tons of foam, or 6000 pounds

    # Calculate the number of pillows Teddy can make
    pillows = total_foam // foam_per_pillow

    # Return the result
    result = pillows
    return result

print(solution())