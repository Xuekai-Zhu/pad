def solution():
    """In Alaska the commercial Cod fishing season runs from January 1 - August 1 lasting exactly 7 months, or 213 days on a non-leap year. Two fishermen are competing against each other to see who can earn more profit. The first fisherman plans to catch fish at a steady rate of 3 per day for the entire season. The second fisherman is a novice who will need to start more slowly. He plans to catch only 1 fish per day during the first 30 days, 2 fish per day during the next 60 days, and then 4 fish per day during the remainder of the season. At the end of the season, how many more fish will be caught by the fisherman who catches the higher number of fish?"""
    season_days = 213
    fisherman1_rate = 3
    fisherman2_rate1 = 1
    fisherman2_rate2 = 2
    fisherman2_rate3 = 4
    days_rate1 = 30
    days_rate2 = 60
    days_rate3 = season_days - days_rate1 - days_rate2
    fisherman1_total = fisherman1_rate * season_days
    fisherman2_total = (fisherman2_rate1 * days_rate1) + (fisherman2_rate2 * days_rate2) + (fisherman2_rate3 * days_rate3)
    more_fish = abs(fisherman1_total - fisherman2_total)
    result = more_fish
    return result

print(solution())