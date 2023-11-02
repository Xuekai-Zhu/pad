def solution():
    pies_per_day = 7  # Cooper makes 7 apple pies a day
    days = 12  # Cooper makes pies for 12 days
    
    # Calculate the total number of pies Cooper makes in 12 days
    total_pies = pies_per_day * days

    # Calculate the number of pies Ashley eats
    pies_eaten = 50

    # Calculate the number of pies remaining with Cooper
    pies_remaining = total_pies - pies_eaten
    result = pies_remaining
    return result

print(solution())