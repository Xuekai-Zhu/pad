def solution():
    # Define initial number of cows
    initial_cows = 51

    # Add 5 cows to the herd
    new_cows = 5
    total_cows = initial_cows + new_cows

    # Calculate the number of cows sold
    cows_sold = total_cows * 0.25

    # Calculate the final number of cows
    remaining_cows = total_cows - cows_sold
    result = remaining_cows
    return result

print(solution())