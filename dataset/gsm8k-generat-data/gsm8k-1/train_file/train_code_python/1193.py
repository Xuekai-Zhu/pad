def solution():
    """Vincent has 72 inches of rope that he wants to use for a project, but he needs to cut it into smaller pieces first. He cuts it into 12 equal length pieces, but then he realizes it's too short, so he ties three pieces together. The knots then make each piece 1 inch shorter. How long are his pieces of rope after all this?"""
    total_length = 72
    num_pieces = 12
    initial_length = total_length / num_pieces
    adjusted_length = initial_length - 1
    
    # Taking into account the 3 pieces tied together
    num_groups = 3
    group_length = adjusted_length * num_groups
    remaining_length = total_length - (initial_length * num_groups)
    final_length = (remaining_length + group_length) / (num_pieces - num_groups)
    
    result = final_length
    return result

print(solution())