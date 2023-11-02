def solution():
    num_cows = 51
    num_new_cows = 5

    # Add the new cows to the herd
    num_cows += num_new_cows

    # Calculate the number of cows to be sold
    num_cows_to_sell = num_cows / 4

    # Subtract the number of cows to be sold from the total number of cows
    num_cows_left = num_cows - num_cows_to_sell
    result = num_cows_left
    return result

print(solution())