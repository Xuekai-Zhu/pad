def solution():
    """In Alaska the commercial Cod fishing season runs from January 1 - August 1 lasting exactly 7 months, or 213 days on a non-leap year.  Two fishermen are competing against each other to see who can earn more profit.  The first fisherman plans to catch fish at a steady rate of 3 per day for the entire season.  The second fisherman is a novice who will need to start more slowly. He plans to catch only 1 fish per day during the first 30 days, 2 fish per day during the next 60 days, and then 4 fish per day during the remainder of the season.  At the end of the season, how many more fish will be caught by the fisherman who catches the higher number of fish?"""
    # Define the total number of days in the fishing season
    total_days = 213

    # Calculate the total number of fish caught by the first fisherman
    fisherman1_fish = 3 * total_days

    # Calculate the total number of fish caught by the second fisherman
    fisherman2_fish = 0
    for i in range(1, total_days+1):
        if i <= 30:
            fisherman2_fish += 1
        elif i <= 90:
            fisherman2_fish += 2
        else:
            fisherman2_fish += 4

    # Calculate the difference in the total number of fish caught by the two fishermen
    fish_difference = abs(fisherman1_fish - fisherman2_fish)

    # Return the result
    result = fish_difference
    return result

print(solution())