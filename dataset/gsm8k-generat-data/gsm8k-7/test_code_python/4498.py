def solution():
    initial_length = 143
    first_cut = 25
    adjustment_cut = 7
    
    # Calculate the length of the board after the first cut
    length_after_first_cut = initial_length - first_cut
    
    # Calculate the total length of the two other boards before adjustment cut
    total_length_before_adj_cut = length_after_first_cut + 2 * adjustment_cut
    
    # Calculate the length of each board before adjustment cut
    length_before_adj_cut = total_length_before_adj_cut / 2
    result = length_before_adj_cut
    return result

print(solution())