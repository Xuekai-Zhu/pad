def solution():
    # Define the time it takes to learn the rules and proficiency level
    time_to_learn = 2 # hours
    time_to_proficiency = 49 * time_to_learn # hours

    # Define the time and cost to become a master
    time_to_master = 100 * (time_to_learn + time_to_proficiency) # hours

    # Calculate the total time spent
    total_time = time_to_learn + time_to_proficiency + time_to_master # hours
    result = total_time
    return result

print(solution())