def solution():
    """A box holds 2 dozen doughnuts. If the family ate 8 doughnuts, how many doughnuts are left?"""
    # Define the number of doughnuts in a box
    DOUGHNUTS_PER_BOX = 24

    # Define the number of doughnuts eaten by the family
    doughnuts_eaten = 8

    # Calculate the number of doughnuts left
    doughnuts_left = DOUGHNUTS_PER_BOX - doughnuts_eaten

    # Display the number of doughnuts left
    result = doughnuts_left
    return result

print(solution())