def solution():
    """Vincent has 72 inches of rope that he wants to use for a project, but he needs to cut it into smaller pieces first. He cuts it into 12 equal length pieces, but then he realizes it's too short, so he ties three pieces together. The knots then make each piece 1 inch shorter. How long are his pieces of rope after all this?"""
    # Define the length of the initial 12 equal pieces
    equal_piece_length = 72 / 12

    # Calculate the length of each piece after tying 3 pieces together and making a knot
    new_piece_length = (equal_piece_length * 3 - 1) / 3

    # Calculate the new length of all the pieces
    new_total_length = new_piece_length * 12

    result = new_total_length
    return result

print(solution())