def solution():
    
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