def solution():
    seven_years_war_start = 1756
    seven_years_war_end = 1763
    ak47_development_year = 1947
    if ak47_development_year > seven_years_war_end:
        result = "no"
    else:
        result = "not applicable"
    return result

print(solution())