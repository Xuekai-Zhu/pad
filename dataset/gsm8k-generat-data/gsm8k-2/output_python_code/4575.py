def solution():
    """Carter is a professional drummer. He goes through 5 sets of drum sticks per show. After the end of each show, he tosses 6 new drum stick sets to audience members. He does this for 30 nights straight. How many sets of drum sticks does he go through?"""
    sets_per_show = 5
    sets_given_away_per_show = 6
    total_shows = 30
    total_sets = (sets_per_show + sets_given_away_per_show) * total_shows
    result = total_sets
    return result

print(solution())