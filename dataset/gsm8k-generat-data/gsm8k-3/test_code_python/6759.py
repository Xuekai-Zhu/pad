def solution():
    """Amaya is watching a movie that she finds kind of boring, so she keeps tuning out and having to rewind it to catch what she missed. She watches 35 minutes before she realizes she needs to rewind the movie to catch something she missed, a process that adds 5 minutes to her total viewing time. She watches the movie for another 45 minutes but has to rewind it again, adding 15 minutes to her total time. Finally, she watches the last 20 minutes uninterrupted. If she added up the duration of the film plus all the times she had to rewind and re-watch parts, how many minutes did it take her to watch the movie?"""
    # Define the duration of the movie and the total time spent rewinding and re-watching parts
    MOVIE_DURATION = 100
    REWIND_TIME_1 = 5
    REWIND_TIME_2 = 15

    # Calculate the total time spent watching the movie
    total_time = MOVIE_DURATION + REWIND_TIME_1 + REWIND_TIME_2 + 35 + 45 + 20

    # Display the total time
    result = total_time
    return result

print(solution())