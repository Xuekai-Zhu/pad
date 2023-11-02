def solution():
    """Leticia, Nina, and Rosalie have a total of 25 people on their dance team. If 8 people quit, but 13 new people got in, how many people are there now on the team?"""
    initial_team_size = 25
    people_quit = 8
    new_people_join = 13
    current_team_size = initial_team_size - people_quit + new_people_join
    result = current_team_size
    return result

print(solution())