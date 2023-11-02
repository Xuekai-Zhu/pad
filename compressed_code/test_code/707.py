def solution():
    
    total_students = 20
    basketball_players = total_students / 2
    volleyball_players = (2/5) * total_students
    both_players = total_students / 10
    neither_players = total_students - (basketball_players + volleyball_players - both_players)
    result = neither_players
    return result

print(solution())