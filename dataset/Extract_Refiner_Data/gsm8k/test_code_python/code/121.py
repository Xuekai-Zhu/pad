def solution():
    
    # Define the number of spoons bought and given to Julia's husband
    spoons_bought = 1 + 5
    spoons_given = 3

    # Calculate the total number of spoons
    total_spoons = 12

    # Calculate the number of spoons used to sample the stew
    spoons_used = spoons_bought + spoons_given

    # Calculate the number of spoons remaining
    spoons_remaining = total_spoons - spoons_used

    # Display the number of spoons remaining
    result = spoons_remaining
    return result

print(solution())