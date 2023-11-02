def solution():
    # Calculate the total number of seeds thrown by Mike
    total_seeds = 20 + 2*20 + 30 + 30  # Mike throws 20 seeds to the birds on the left, twice as much to the bigger group on the right, 30 more to the additional birds, and has 30 seeds left for the last birds
    result = total_seeds + 30  # add the 30 seeds left for the last birds to get the total number of seeds Mike started with
    return result

print(solution())