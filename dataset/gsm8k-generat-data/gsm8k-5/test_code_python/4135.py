def solution():
    total_teeth = 4 * 32  # Four adults with 32 teeth each
    teeth_removed_1 = 1/4 * total_teeth  # First person has 1/4 of all teeth removed
    teeth_removed_2 = 3/8 * total_teeth  # Second person has 3/8 of all teeth removed
    teeth_removed_3 = 1/2 * total_teeth  # Third person has 1/2 of all teeth removed
    teeth_removed_4 = 4  # Fourth person has 4 teeth removed

    # Calculate the total number of teeth removed
    total_teeth_removed = teeth_removed_1 + teeth_removed_2 + teeth_removed_3 + teeth_removed_4
    result = total_teeth_removed
    return result

print(solution())