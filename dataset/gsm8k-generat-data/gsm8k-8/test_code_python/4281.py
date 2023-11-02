def solution():
    # Define the variables
    pond_capacity = 200
    pumping_rate = 6 * (2/3) # Reduced pumping rate due to drought restrictions
    time_to_fill_pond = pond_capacity / pumping_rate
    result = time_to_fill_pond
    return result

print(solution())