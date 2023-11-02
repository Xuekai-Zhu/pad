def solution():
    num_pies_per_day = 7
    num_days = 12
    num_pies_eaten = 50

    # Calculate the total number of pies Cooper makes
    total_pies_made = num_pies_per_day * num_days

    # Calculate the number of pies remaining with Cooper
    num_pies_remaining = total_pies_made - num_pies_eaten
    result = num_pies_remaining
    return result

print(solution())