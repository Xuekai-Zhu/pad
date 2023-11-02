def solution():
    """The town is having a race to see who can run around the town square 7 times the fastest. The town square is 3/4 of a mile long. The winner finishes the race in 42 minutes. Last year's winner finished in 47.25 minutes. How many minutes on average faster did this year's winner run one mile of the race compared to last year?"""
    # Calculate the total distance of the race
    distance = 7 * 3/4  # 7 times around the town square

    # Calculate the time taken by the winner to complete one mile
    winner_time_per_mile = 42/(distance)  

    # Calculate the time taken by last year's winner to complete one mile
    last_year_winner_time_per_mile = 47.25/(distance)

    # Calculate the difference in time taken per mile by the two winners
    time_difference = last_year_winner_time_per_mile - winner_time_per_mile

    # Display the time difference
    result = time_difference
    return result

print(solution())