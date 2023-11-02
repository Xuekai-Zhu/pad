def solution():
    """The town is having a race to see who can run around the town square 7 times the fastest. The town square is 3/4 of a mile long. The winner finishes the race in 42 minutes. Last year's winner finished in 47.25 minutes. How many minutes on average faster did this year's winner run one mile of the race compared to last year?"""
    laps = 7
    square_length = 3/4
    race_length = laps * square_length
    this_year_time = 42
    last_year_time = 47.25
    this_year_mile_time = this_year_time / race_length
    last_year_mile_time = last_year_time / race_length
    time_difference = last_year_mile_time - this_year_mile_time
    result = time_difference
    return result

print(solution())