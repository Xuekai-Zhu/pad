def solution():
    """Of the 600 students at River Falls High School, 3/4 of them play tennis. Of those that play tennis, 60% of them also play hockey. How many students play both hockey and tennis?"""
    total_students = 600
    tennis_players = (3/4) * total_students
    hockey_and_tennis_players = 0.6 * tennis_players
    result = hockey_and_tennis_players
    return result

print(solution())