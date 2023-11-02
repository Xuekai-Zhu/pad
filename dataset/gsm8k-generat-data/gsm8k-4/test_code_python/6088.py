def solution():
    """Kim has 4 dozen shirts. She lets her sister have 1/3 of them. How many shirts does she have left?"""
    # Define the initial number of shirts
    initial_shirts = 4 * 12

    # Calculate the number of shirts given to her sister
    sister_shirts = initial_shirts * (1/3)

    # Calculate the number of shirts left with Kim
    shirts_left = initial_shirts - sister_shirts

    result = shirts_left
    return result

print(solution())