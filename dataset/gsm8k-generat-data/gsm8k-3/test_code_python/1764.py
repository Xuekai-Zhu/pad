def solution():
    """In Alaska the commercial Cod fishing season runs from January 1 - August 1 lasting exactly 7 months,
    or 213 days on a non-leap year. Two fishermen are competing against each other to see who can earn more profit.
    The first fisherman plans to catch fish at a steady rate of 3 per day for the entire season.
    The second fisherman is a novice who will need to start more slowly.
    He plans to catch only 1 fish per day during the first 30 days, 2 fish per day during the next 60 days,
    and then 4 fish per day during the remainder of the season.
    At the end of the season, how many more fish will be caught by the fisherman who catches the higher number of fish?"""
    
    # Define the season length
    season_days = 213

    # Calculate the number of fish caught by the first fisherman
    fisherman1_catch = 3 * season_days

    # Calculate the number of fish caught by the second fisherman
    fisherman2_catch = 0
    for i in range(season_days):
        if i < 30:
            fisherman2_catch += 1
        elif i < 90:
            fisherman2_catch += 2
        else:
            fisherman2_catch += 4

    # Calculate the difference in number of fish caught
    difference = abs(fisherman1_catch - fisherman2_catch)

    # Display the difference in number of fish caught
    result = difference
    return result

print(solution())