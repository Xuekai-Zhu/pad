def solution():
    # Calculate the time needed for the injury to fully heal
    full_healing_time = 3 * 5

    # Calculate the total time until James can start working out again
    total_time = full_healing_time + 3

    # Calculate the time until James can start lifting heavy again
    lifting_time = total_time + 3 * 7

    result = lifting_time
    return result

print(solution())