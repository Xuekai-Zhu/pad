def solution():
    
    total_students = 20
    basketball_players = total_students / 2
    volleyball_players = (2 / 5) * total_students
    basketball_and_volleyball = total_students / 10
    neither = total_students - basketball_players - volleyball_players + basketball_and_volleyball
    result = neither
    return result

print(solution())