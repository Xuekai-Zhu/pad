def solution():
    
    # Define the number of punches thrown per minute and the duration of each round
    PUNCHES_PER_MINUTE = 25
    TIME_PER_ROUND = 3

    # Calculate the total duration of the fight
    total_duration = 5 * TIME_PER_ROUND

    # Calculate the total number of punches thrown
    total_punches = PUNCHES_PER_MINUTE * total_duration

    # Display the total number of punches thrown
    result = total_punches
    return result

print(solution())