def solution():
    """Celia runs twice as fast as Lexie. If it takes Lexie 20 minutes to run a mile, how long, in minutes, will it take Celia to run 30 miles?"""
    lexie_time_per_mile = 20
    cecilia_speed_ratio = 2
    miles_to_run = 30

    # calculate Celia's time per mile
    cecilia_time_per_mile = lexie_time_per_mile / cecilia_speed_ratio

    # calculate total time for Celia to run 30 miles
    total_time = miles_to_run * cecilia_time_per_mile

    result = total_time
    return result

print(solution())