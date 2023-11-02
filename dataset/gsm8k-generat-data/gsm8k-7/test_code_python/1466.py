def solution():
    num_dogs = 2
    barks_per_minute = 30
    total_minutes = 10

    # Calculate the total number of barks per minute for all dogs
    total_barks_per_minute = num_dogs * barks_per_minute

    # Calculate the total number of barks after 10 minutes
    total_barks = total_barks_per_minute * total_minutes
    result = total_barks
    return result

print(solution())