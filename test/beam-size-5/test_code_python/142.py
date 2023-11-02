def solution():
    
    # Define the number of pieces on the floor
    floor_pieces = 500

    # Calculate the number of pieces on the first lego boxed
    first_lego_pieces = floor_pieces * 3

    # Calculate the number of pieces on the second lego boxed
    second_lego_pieces = floor_pieces * 1/4

    # Calculate the total number of blocks Johnny picked up
    total_blocks = first_lego_pieces + second_lego_pieces + third_lego_pieces

    # Display the total number of blocks
    result = total_blocks
    return result

print(solution())