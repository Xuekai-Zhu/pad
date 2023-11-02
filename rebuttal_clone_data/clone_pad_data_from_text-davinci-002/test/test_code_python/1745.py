def solution():
    initial_fish = 2
    fish_per_year = 2
    death_rate = 1
    fish_after_5_years = initial_fish + (5 * fish_per_year) - (5 * death_rate)
    result = fish_after_5_years
    return result

print(solution())