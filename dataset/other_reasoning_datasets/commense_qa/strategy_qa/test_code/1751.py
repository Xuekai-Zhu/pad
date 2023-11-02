def solution():
    mating_season_months = ["June", "July"]
    fasting_recommendation = True
    if "July" in mating_season_months and not fasting_recommendation:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())