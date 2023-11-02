def solution():
    """There were 50 racers in a bicycle charity race at the beginning of the race. After 20 minutes, 30 more racers joined the race. The total number of racers doubled after another 30 minutes. If at the end of the race only 130 people finished the race, what's the total number of people who dropped before finishing the race?"""
    # Define the initial number of racers and the time intervals
    initial_racers = 50
    time_interval_1 = 20
    time_interval_2 = 30

    # Calculate the number of racers who joined the race after 20 minutes
    joined_racers = 30

    # Calculate the total number of racers after 20 minutes
    total_racers_20min = initial_racers + joined_racers

    # Calculate the total number of racers after 50 minutes
    total_racers_50min = total_racers_20min * 2

    # Calculate the number of racers who dropped out before finishing the race
    dropouts = total_racers_50min - 130

    # Return the result
    result = dropouts
    return result

print(solution())