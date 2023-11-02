def solution():
    """Gina chooses what she and her sister will watch on Netflix three times as often as her sister does.
    If her sister watches a total of 24 shows on Netflix per week, and each show is 50 minutes long,
    how many minutes of Netflix does Gina get to choose?"""
    sister_shows = 24
    gina_shows = sister_shows * 3
    total_shows = sister_shows + gina_shows
    minutes_per_show = 50
    gina_minutes = gina_shows * minutes_per_show
    result = gina_minutes
    return result

print(solution())