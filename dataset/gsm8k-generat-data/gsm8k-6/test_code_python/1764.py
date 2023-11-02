def solution():
    season_days = 213
    rate_fisherman1 = 3
    rate_fisherman2 = [1]*30 + [2]*60 + [4]*(season_days-90)

    total_fish_fisherman1 = rate_fisherman1 * season_days
    total_fish_fisherman2 = sum(rate_fisherman2)

    difference = total_fish_fisherman1 - total_fish_fisherman2
    result = abs(difference)
    return result

print(solution())