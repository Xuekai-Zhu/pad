def solution():
    """Jordan has a new hit song on Spotify. 3 months are left in the year, and she currently has 60,000 listens. If the number of listens per month doubles, how many listens will the song have by the end of the year?"""
    current_listens = 60000
    remaining_months = 3
    listens_per_month = current_listens / (2 ** (remaining_months - 1))
    total_listens = current_listens + (listens_per_month * remaining_months)
    result = total_listens
    return result

print(solution())