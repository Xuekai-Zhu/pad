def solution():
    michael_trophies = 30  # Michael currently has 30 trophies
    michael_trophies_in_3_years = michael_trophies + 100  # Michael will have 100 more trophies in three years
    jack_trophies_in_3_years = 10 * michael_trophies_in_3_years  # Jack will have ten times more trophies than Michael in three years

    # Calculate the total number of trophies they will have altogether in three years
    total_trophies = michael_trophies_in_3_years + jack_trophies_in_3_years
    result = total_trophies
    return result

print(solution())