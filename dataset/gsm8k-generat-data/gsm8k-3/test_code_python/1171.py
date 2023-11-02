def solution():
    """Jack will have ten times more handball trophies than Michael has right now in three years. If Michael has 30 trophies right now, and the number of his trophies increases by 100 in three years, what's the total number of trophies they'll have altogether after three years?"""
    # Michael's current number of trophies
    michael_trophies = 30

    # Michael's number of trophies in three years
    michael_trophies_3_years = michael_trophies + 100

    # Jack's number of trophies in three years
    jack_trophies_3_years = 10 * michael_trophies_3_years

    # Total number of trophies in three years
    total_trophies = michael_trophies_3_years + jack_trophies_3_years

    # Display the total number of trophies
    result = total_trophies
    return result

print(solution())