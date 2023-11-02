def solution():
    """Jack will have ten times more handball trophies than Michael has right now in three years. If Michael has 30 trophies right now, and the number of his trophies increases by 100 in three years, what's the total number of trophies they'll have altogether after three years?"""
    michael_trophies_now = 30
    michael_trophies_in_3yrs = michael_trophies_now + 100
    jack_trophies_in_3yrs = 10 * michael_trophies_in_3yrs
    total_trophies_in_3yrs = michael_trophies_in_3yrs + jack_trophies_in_3yrs
    result = total_trophies_in_3yrs
    return result

print(solution())