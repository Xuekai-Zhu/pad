def solution():
    michael_trophies = 30
    michael_trophies_in_three_years = michael_trophies + 100
    jack_trophies_in_three_years = 10 * michael_trophies_in_three_years
    total_trophies = michael_trophies_in_three_years + jack_trophies_in_three_years
    result = total_trophies
    return result

print(solution())