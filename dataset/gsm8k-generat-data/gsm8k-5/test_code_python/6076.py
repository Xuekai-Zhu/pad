def solution():
    initial_cows = 51  # The farmer has 51 cows initially
    new_cows = 5  # The farmer adds 5 new cows to the herd

    # Calculate the total number of cows after adding the new cows
    total_cows = initial_cows + new_cows

    # Calculate the number of cows to be sold
    cows_to_be_sold = total_cows / 4

    # Calculate the number of cows remaining
    remaining_cows = total_cows - cows_to_be_sold
    result = remaining_cows
    return result

print(solution())