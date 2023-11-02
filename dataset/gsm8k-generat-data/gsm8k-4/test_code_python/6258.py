def solution():
    """Jordan has a new hit song on Spotify. 3 months are left in the year, and she currently has 60,000 listens. If the number of listens per month doubles, how many listens will the song have by the end of the year?"""
    # Define the initial number of listens and the remaining number of months
    initial_listens = 60000
    remaining_months = 3

    # Double the number of listens each month for the remaining number of months
    for i in range(remaining_months):
        initial_listens *= 2

    # return the result
    result = initial_listens
    return result

print(solution())