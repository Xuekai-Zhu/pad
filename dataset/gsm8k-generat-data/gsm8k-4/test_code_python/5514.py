def solution():
    """A cooler is filled with 24 cans of cherry soda and orange pop. If there are twice as many cans of orange pop as there are of cherry soda, how many cherry sodas are there?"""
    # Define the number of cherry soda cans as x
    x = None

    # Define the number of orange pop cans as 2x
    orange_pop = 2 * x

    # Calculate the total number of cans
    total_cans = x + orange_pop

    # Check that the total number of cans is 24
    while total_cans != 24:
        # If the total number of cans is greater than 24, decrease the number of orange pop cans
        if total_cans > 24:
            orange_pop -= 1
        # If the total number of cans is less than 24, increase the number of orange pop cans
        else:
            x += 1
            orange_pop = 2 * x
        
        # Recalculate the total number of cans
        total_cans = x + orange_pop

    # Return the number of cherry soda cans    
    result = x
    return result

print(solution())