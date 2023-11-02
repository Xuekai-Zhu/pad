def solution():
    # Calculate the total length of the first 3 podcasts
    total_length = 45 + 2*45 + 105

    # Calculate the total length of all 4 podcasts
    total_length += 60

    # Calculate the remaining time for the next podcast
    remaining_time = 6*60 - total_length

    # Convert remaining time to hours
    remaining_hours = remaining_time / 60

    result = remaining_hours
    return result

print(solution())