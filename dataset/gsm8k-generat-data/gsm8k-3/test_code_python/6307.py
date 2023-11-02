def solution():
    """Michael was watching a TV show, which was aired for 1.5 hours. During this time, there were 3 commercials, which lasted 10 minutes each. How long (in hours) was the TV show itself, not counting commercials?"""
    # Convert the total time to minutes
    total_time = 1.5 * 60

    # Calculate the total time of the commercials
    commercials_time = 3 * 10

    # Calculate the time of the TV show without commercials
    tv_show_time = total_time - commercials_time

    # Convert the time of the TV show back to hours
    tv_show_hours = tv_show_time / 60

    # Display the result
    result = tv_show_hours
    return result

print(solution())