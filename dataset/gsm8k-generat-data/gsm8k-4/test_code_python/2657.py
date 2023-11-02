def solution():
    """A box holds 2 dozen doughnuts. If the family ate 8 doughnuts, how many doughnuts are left?"""
    # Define the initial number of doughnuts
    initial_doughnuts = 2 * 12

    # Define the number of doughnuts eaten
    eaten_doughnuts = 8

    # Calculate the number of doughnuts left
    doughnuts_left = initial_doughnuts - eaten_doughnuts

    # Return the result
    result = doughnuts_left
    return result

print(solution())