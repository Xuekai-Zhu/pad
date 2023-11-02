def solution():
    
    initial_flock_size = 100
    annual_change = 10
    num_years = 5
    current_flock_size = initial_flock_size + (annual_change * num_years)
    combined_flock_size = current_flock_size + 150
    result = combined_flock_size
    return result

print(solution())