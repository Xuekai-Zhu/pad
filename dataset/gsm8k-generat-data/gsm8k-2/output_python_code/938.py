def solution():
    """There are 20 students in the class. Half of them play basketball. Two-fifths play volleyball and one-tenth play both basketball and volleyball. How many students in this class do not play either game?"""
    total_students = 20
    basketball_players = total_students / 2
    volleyball_players = (2/5) * total_students
    both_players = total_students / 10
    neither_players = total_students - (basketball_players + volleyball_players - both_players)
    result = neither_players
    return result

print(solution())