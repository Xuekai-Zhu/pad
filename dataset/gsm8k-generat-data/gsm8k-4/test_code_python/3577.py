def solution():
    """The town is having a race to see who can run around the town square 7 times the fastest. The town square is 3/4 of a mile long. The winner finishes the race in 42 minutes. Last year's winner finished in 47.25 minutes. How many minutes on average faster did this year's winner run one mile of the race compared to last year?"""
    # Calculate the total distance of the race
    distance = (3/4) * 7

    # Calculate the speed of last year's winner
    speed_last_year = distance / (47.25 / 60)

    # Calculate the speed of this year's winner
    speed_this_year = distance / (42 / 60)

    # Calculate the difference in speed
    speed_difference = speed_last_year - speed_this_year

    # Calculate the time difference for one mile
    time_difference = (1 / speed_last_year) - (1 / speed_this_year)

    # Convert the time difference to minutes
    time_difference = time_difference * 60

    result = time_difference
    return result

print(solution())