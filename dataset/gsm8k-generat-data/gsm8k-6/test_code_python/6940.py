def solution():
    # Calculate the total airing time of the 6 programs
    total_airing_time = 6 * 30  # there are 6 thirty-minute programs

    # Calculate the total time spent on commercials
    time_spent_on_commercials = total_airing_time / 4  # one-fourth of airing time is spent on commercials

    # Convert the time spent on commercials to minutes
    minutes_spent_on_commercials = time_spent_on_commercials * 60

    result = minutes_spent_on_commercials
    return result

print(solution())