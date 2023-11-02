def solution():
    """Of the 600 students at River Falls High School, 3/4 of them play tennis. Of those that play tennis, 60% of them also play hockey. How many students play both hockey and tennis?"""
    total_students = 600
    tennis_players = total_students * 3/4
    hockey_and_tennis_players = tennis_players * 0.6
    result = hockey_and_tennis_players
    return result

print(solution())