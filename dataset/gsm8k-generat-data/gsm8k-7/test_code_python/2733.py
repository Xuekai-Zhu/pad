def solution():
    initial_size = 100
    annual_loss = 20
    annual_births = 30
    num_years = 5
    other_flock_size = 150

    # Calculate the size of the original flock after the given number of years
    final_size = initial_size + (annual_births - annual_loss) * num_years

    # Calculate the total size of the combined flock
    total_size = final_size + other_flock_size
    result = total_size
    return result

print(solution())