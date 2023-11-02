def solution():
    # Define the number of pills taken each day for the first 2 days
    pills_per_day_1_2 = 2 * 3
    
    # Define the number of pills taken each day for the next 3 days
    pills_per_day_3_5 = (2 * 3) / 2
    
    # Define the total number of pills taken over the 6 days
    total_pills_taken = (pills_per_day_1_2 * 2) + (pills_per_day_3_5 * 3) + 2
    
    # Define the number of pills left in the bottle
    pills_left = 50 - total_pills_taken
    
    result = pills_left
    return result

print(solution())