def solution():
    """Vincent has 72 inches of rope that he wants to use for a project, but he needs to cut it into smaller pieces first. He cuts it into 12 equal length pieces, but then he realizes it's too short, so he ties three pieces together. The knots then make each piece 1 inch shorter. How long are his pieces of rope after all this?"""
    
    # Calculate the length of each original piece of rope
    piece_length = 72 / 12

    # Calculate the length of each piece after tying three pieces together
    new_piece_length = (3 * piece_length - 3) / 3

    # Calculate the length of each piece after tying three pieces together and accounting for the lost length due to the knots
    final_piece_length = new_piece_length - 1

    # Display the final length of each piece of rope
    result = final_piece_length
    return result

print(solution())