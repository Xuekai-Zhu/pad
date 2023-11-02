def solution():
    """The Lady Eagles basketball team scored a total of 311 points in 5 games. Some players combined for 188 points. Lisa, Jessie, and Devin equally scored the rest. How many points did Jessie score?"""
    total_points = 311
    some_players_points = 188
    remaining_points = total_points - some_players_points
    jessie_points = remaining_points / 3
    result = jessie_points
    return result

print(solution())