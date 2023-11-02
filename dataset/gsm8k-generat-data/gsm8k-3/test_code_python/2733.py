def solution():
    """Every year 20 ducks from a flock are killed but another 30 are born.  The original flock size is 100 ducks.  After 5 years they join with another flock of 150 ducks.  How many ducks are in the combined flock?"""
    # Define the initial flock size and the annual changes in the flock
    INITIAL_SIZE = 100
    ANNUAL_DEATHS = 20
    ANNUAL_BIRTHS = 30

    # Calculate the size of the original flock after 5 years
    final_size = INITIAL_SIZE + (ANNUAL_BIRTHS - ANNUAL_DEATHS) * 5

    # Calculate the size of the combined flock
    combined_size = final_size + 150

    # Display the size of the combined flock
    result = combined_size
    return result

print(solution())