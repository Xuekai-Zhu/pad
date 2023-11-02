def solution():
    total_students = 20
    basketball_players = total_students / 2
    volleyball_players = (2/5) * total_students
    basketball_and_volleyball_players = total_students / 10

    non_players = total_students - (basketball_players + volleyball_players - basketball_and_volleyball_players)
    result = non_players
    return result

print(solution())