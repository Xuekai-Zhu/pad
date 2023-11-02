def solution():
    """Jack will have ten times more handball trophies than Michael has right now in three years. If Michael has 30 trophies right now, and the number of his trophies increases by 100 in three years, what's the total number of trophies they'll have altogether after three years?"""
    # Define Michael's current number of trophies
    michael_trophies_now = 30

    # Calculate Michael's number of trophies in three years
    michael_trophies_future = michael_trophies_now + 100

    # Calculate Jack's number of trophies in three years (10 times more than Michael's number of trophies)
    jack_trophies_future = 10 * michael_trophies_future

    # Calculate the total number of trophies in three years
    total_trophies_future = michael_trophies_future + jack_trophies_future

    # return the result
    result = total_trophies_future
    return result

print(solution())