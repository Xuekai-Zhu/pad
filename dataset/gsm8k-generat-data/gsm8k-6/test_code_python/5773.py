def solution():
    # Find the number of gnomes in Ravenswood forest
    num_gnomes_Ravenswood = 4 * 20  # four times as many gnomes as in Westerville woods
    
    # Calculate the number of gnomes taken by the forest owner
    num_gnomes_taken = 0.4 * num_gnomes_Ravenswood
    
    # Calculate the remaining number of gnomes in Ravenswood forest
    num_gnomes_remaining = num_gnomes_Ravenswood - num_gnomes_taken
    
    result = num_gnomes_remaining
    return result

print(solution())