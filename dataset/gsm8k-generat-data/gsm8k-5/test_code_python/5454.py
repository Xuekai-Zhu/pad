def solution():
    starting_stamps = 40  # Maria has 40 stamps in her collection
    percentage_increase = 0.2  # Maria wants to increase her collection by 20%
    
    # Calculate the total number of stamps Maria wants to collect
    total_stamps = starting_stamps + (starting_stamps * percentage_increase)
    result = total_stamps
    return result

print(solution())