def solution():
    """Every year 20 ducks from a flock are killed but another 30 are born. The original flock size is 100 ducks. After 5 years they join with another flock of 150 ducks. How many ducks are in the combined flock?"""
    initial_flock_size = 100
    annual_change = 10
    num_years = 5
    current_flock_size = initial_flock_size + (annual_change * num_years)
    combined_flock_size = current_flock_size + 150
    result = combined_flock_size
    return result

print(solution())