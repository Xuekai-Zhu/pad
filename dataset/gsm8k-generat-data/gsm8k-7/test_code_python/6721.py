def solution():
    initial_height = 52
    growth_per_year = 5
    years = 8
    inches_per_foot = 12
    
    # Calculate the total growth in feet over 8 years
    total_growth_feet = growth_per_year * years
    
    # Add the initial height to the total growth to get the final height in feet
    final_height_feet = initial_height + total_growth_feet
    
    # Convert the final height into inches
    final_height_inches = final_height_feet * inches_per_foot
    
    result = final_height_inches
    return result

print(solution())