def solution():
    """Michael was watching a TV show, which was aired for 1.5 hours. During this time, there were 3 commercials, which lasted 10 minutes each. How long (in hours) was the TV show itself, not counting commercials?"""
    # Define the airing time of the TV show in hours
    tv_show_time = 1.5

    # Define the total time taken by the commercials in minutes
    commercials_time = 3 * 10

    # Convert commercials time to hours
    commercials_time_hours = commercials_time / 60

    # Calculate the TV show time without commercials
    tv_show_time_no_commercials = tv_show_time - commercials_time_hours

    result = tv_show_time_no_commercials
    return result

print(solution())