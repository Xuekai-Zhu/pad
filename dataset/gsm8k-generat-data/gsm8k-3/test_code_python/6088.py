def solution():
    """Kim has 4 dozen shirts.  She lets her sister have 1/3 of them.  How many shirts does she have left?"""
    # Define the number of dozens of shirts Kim has
    kim_shirts_dozens = 4

    # Calculate the total number of shirts Kim has
    kim_shirts_total = kim_shirts_dozens * 12

    # Calculate the number of shirts Kim's sister takes
    sister_shirts = kim_shirts_total / 3

    # Calculate the number of shirts Kim has left
    kim_shirts_left = kim_shirts_total - sister_shirts

    # Display the number of shirts Kim has left
    result = kim_shirts_left
    return result

print(solution())