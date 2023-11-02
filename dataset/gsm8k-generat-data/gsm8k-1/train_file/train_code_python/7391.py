def solution():
    """Gina chooses what she and her sister will watch on Netflix three times as often as her sister does. If her sister watches a total of 24 shows on Netflix per week, and each show is 50 minutes long, how many minutes of Netflix does Gina get to choose?"""
    sister_shows_per_week = 24
    gina_shows_per_week = sister_shows_per_week * 3
    show_length = 50
    gina_total_minutes = gina_shows_per_week * show_length
    result = gina_total_minutes
    return result

print(solution())