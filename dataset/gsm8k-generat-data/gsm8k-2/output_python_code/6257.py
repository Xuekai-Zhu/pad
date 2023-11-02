def solution():
    """Jordan has a new hit song on Spotify. 3 months are left in the year, and she currently has 60,000 listens. If the number of listens per month doubles, how many listens will the song have by the end of the year?"""
    current_listens = 60000
    remaining_months = 3
    total_listens = current_listens
    for i in range(remaining_months):
        total_listens *= 2
    result = total_listens
    return result

print(solution())