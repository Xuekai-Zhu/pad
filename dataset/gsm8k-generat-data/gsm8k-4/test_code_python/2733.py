def solution():
    """Every year 20 ducks from a flock are killed but another 30 are born. The original flock size is 100 ducks.
    After 5 years they join with another flock of 150 ducks. How many ducks are in the combined flock?"""
    
    # Initialize the number of ducks in the original flock
    ducks_in_flock = 100

    # Simulate the growth and mortality of the flock over 5 years
    for i in range(5):
        ducks_in_flock += 10  # 30 new ducks are born, 20 are killed
    combined_flock = ducks_in_flock + 150
    
    result = combined_flock
    return result

print(solution())