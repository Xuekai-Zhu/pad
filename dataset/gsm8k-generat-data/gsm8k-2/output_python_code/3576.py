def solution():
    """The town is having a race to see who can run around the town square 7 times the fastest. The town square is 3/4 of a mile long. The winner finishes the race in 42 minutes. Last year's winner finished in 47.25 minutes. How many minutes on average faster did this year's winner run one mile of the race compared to last year?"""
    distance = 7 * (3/4)
    this_year_time = 42
    last_year_time = 47.25
    this_year_speed = distance / (this_year_time / 60)
    last_year_speed = distance / (last_year_time / 60)
    difference = last_year_speed - this_year_speed
    result = difference
    return result

print(solution())