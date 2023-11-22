def solution():
    
    # Define the number of pieces in each lego boxed set
    lego_pieces = 500

    # Calculate the number of pieces in the second lego boxed set
    leg2_pieces = lego_pieces * 3

    # Calculate the number of pieces in the third lego boxed set
    leg3_pieces = leg2_pieces / 4

    # Calculate the total number of lego pieces
    total_leg_pieces = lego_pieces + leg2_pieces + leg3_pieces

    # Calculate the total number of blocks picked up
    total_blocks = total_leg_pieces * 2

    # return the result
    result = total_blocks
    return result

print(solution())