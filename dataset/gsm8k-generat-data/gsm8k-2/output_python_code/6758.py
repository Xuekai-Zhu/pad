def solution():
    """Amaya is watching a movie that she finds kind of boring, so she keeps tuning out and having to rewind it to catch what she missed. She watches 35 minutes before she realizes she needs to rewind the movie to catch something she missed, a process that adds 5 minutes to her total viewing time. She watches the movie for another 45 minutes but has to rewind it again, adding 15 minutes to her total time. Finally, she watches the last 20 minutes uninterrupted. If she added up the duration of the film plus all the times she had to rewind and re-watch parts, how many minutes did it take her to watch the movie?"""
    movie_duration = 35 + 45 + 20
    total_rewind_time = 5 + 15
    total_time = movie_duration + total_rewind_time
    result = total_time
    return result

print(solution())