def solution():
    total_time = 6  # Roger has a 6-hour drive planned out
    used_time = (45/60) + ((45*2)/60) + (1.75) + 1  # Roger has already used this much time listening to podcasts
    remaining_time = total_time - used_time  # Roger needs to fill up the remaining time with podcasts

    # Calculate the required length of the next podcast
    required_length = remaining_time * 60  # Convert remaining time to minutes

    result = required_length / 60  # Convert required length back to hours
    return result

print(solution())