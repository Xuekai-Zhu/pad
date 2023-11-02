def solution():
    gervais_miles_per_day = 315/3  # average miles per day for Gervais
    henri_miles_per_day = 1250/7  # average miles per day for Henri

    # Calculate the difference in miles driven per day between Henri and Gervais
    difference = henri_miles_per_day - gervais_miles_per_day
    
    # Calculate the total difference in miles driven over the 3 days
    total_difference = difference * 3
    
    result = total_difference
    return result

print(solution())