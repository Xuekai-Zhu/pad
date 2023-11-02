def solution():
    total_show_time = 1.5  # The TV show is aired for 1.5 hours
    commercials_time = 3 * 10 / 60  # There are 3 commercials, each lasting 10 minutes

    # Calculate the total time of the TV show without commercials
    show_time = total_show_time - commercials_time
    result = show_time
    return result

print(solution())