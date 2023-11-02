def solution():
    initial_screws = 8
    num_needed = initial_screws * 2
    num_piles = 4

    # Calculate the total number of screws needed
    total_screws = initial_screws + num_needed

    # Calculate the number of screws in each pile
    num_per_pile = total_screws / num_piles
    result = num_per_pile
    return result

print(solution())