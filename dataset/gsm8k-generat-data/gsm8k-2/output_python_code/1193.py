def solution():
    """Vincent has 72 inches of rope that he wants to use for a project, but he needs to cut it into smaller pieces first. He cuts it into 12 equal length pieces, but then he realizes it's too short, so he ties three pieces together. The knots then make each piece 1 inch shorter. How long are his pieces of rope after all this?"""
    total_length = 72
    num_pieces = 12
    piece_length = total_length / num_pieces
    tied_pieces_length = piece_length * 3 - 3
    final_length = piece_length - 1 + tied_pieces_length
    result = final_length
    return result

print(solution())