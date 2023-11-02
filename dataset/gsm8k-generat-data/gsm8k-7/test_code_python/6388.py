def solution():
    final_num_cans = 24
    amount_taken = 6
    
    # Calculate the number of cans Tim had left after Jeff took some
    num_cans_left = final_num_cans + amount_taken
    
    # Calculate the original number of cans Tim had
    original_num_cans = 2 * num_cans_left
    
    result = original_num_cans
    return result

print(solution())