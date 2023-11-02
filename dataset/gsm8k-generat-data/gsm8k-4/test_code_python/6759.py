def solution():
    """Amaya is watching a movie that she finds kind of boring, so she keeps tuning out and having to rewind it to catch what she missed. She watches 35 minutes before she realizes she needs to rewind the movie to catch something she missed, a process that adds 5 minutes to her total viewing time. She watches the movie for another 45 minutes but has to rewind it again, adding 15 minutes to her total time. Finally, she watches the last 20 minutes uninterrupted. If she added up the duration of the film plus all the times she had to rewind and re-watch parts, how many minutes did it take her to watch the movie?"""
    # Define the duration of each segment of the movie
    first_segment = 35
    second_segment = 45
    third_segment = 20

    # Define the time added due to rewinding in each segment
    first_rewind = 5
    second_rewind = 15

    # Add up the total duration of the movie plus the rewinding time
    total_time = first_segment + second_segment + third_segment + first_rewind + second_rewind

    result = total_time
    return result

print(solution())