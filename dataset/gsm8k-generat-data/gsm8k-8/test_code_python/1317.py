def solution():
    # Define the variables
    carlos_time = 3 # in minutes, to convert to seconds later
    diego_distance = 0.5 # as he ran half the block
    diego_time = 2.5 # in minutes, to convert to seconds later

    # Convert Carlos' time to seconds
    carlos_time_seconds = carlos_time * 60

    # Calculate Diego's speed in order to find how long it would take him to run the entire block
    diego_speed = diego_distance / (diego_time / 60) # convert minutes to seconds
    diego_time_total = (1 / diego_speed) * 60 # in seconds

    # Calculate the average time
    total_time_seconds = carlos_time_seconds + diego_time_total
    average_time_seconds = total_time_seconds / 2
    result = average_time_seconds
    return result

print(solution())