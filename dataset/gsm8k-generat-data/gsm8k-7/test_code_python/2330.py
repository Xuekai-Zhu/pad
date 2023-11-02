def solution():
    mural_length = 20
    mural_width = 15
    time_per_square_foot = 20  # minutes
    rate_per_hour = 150
    
    # Calculate the total area of the mural
    mural_area = mural_length * mural_width
    
    # Convert time per square foot to time for entire mural
    time_for_mural = time_per_square_foot * mural_area  # minutes
    
    # Convert time for mural to hours
    time_for_mural_hours = time_for_mural / 60  # hours
    
    # Calculate the total cost for painting the mural
    total_cost = time_for_mural_hours * rate_per_hour
    result = total_cost
    return result

print(solution())