def solution():
    """
    In Alaska, the commercial Cod fishing season runs from January 1 - August 1 lasting exactly 213 days on a non-leap year.
    Two fishermen are competing against each other to see who can earn more profit. The first fisherman plans to catch fish at
    a steady rate of 3 per day for the entire season. The second fisherman is a novice who will need to start more slowly. He
    plans to catch only 1 fish per day during the first 30 days, 2 fish per day during the next 60 days, and then 4 fish per 
    day during the remainder of the season. At the end of the season, how many more fish will be caught by the fisherman who 
    catches the higher number of fish?
    """
    season_days = 213
    first_fisherman_rate = 3
    second_fisherman_rate_stage_1 = 1
    second_fisherman_rate_stage_2 = 2
    second_fisherman_rate_stage_3 = 4
    
    # calculate total number of fish caught by first fisherman
    first_fisherman_fish_caught = first_fisherman_rate * season_days
    
    # calculate total number of fish caught by second fisherman
    second_fisherman_fish_caught = 0
    for day in range(1, season_days+1):
        if day <= 30:
            second_fisherman_fish_caught += second_fisherman_rate_stage_1
        elif day <= 90:
            second_fisherman_fish_caught += second_fisherman_rate_stage_2
        else:
            second_fisherman_fish_caught += second_fisherman_rate_stage_3
    
    # calculate the difference in fish caught
    fish_difference = abs(first_fisherman_fish_caught - second_fisherman_fish_caught)
    
    result = fish_difference
    return result

print(solution())