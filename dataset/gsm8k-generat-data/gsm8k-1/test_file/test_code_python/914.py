def solution():
    """There are 6 students playing tennis and twice that number playing volleyball. There are 16 boys and 22 girls playing soccer. If each student only participates in one group, how many students are there in total?"""
    tennis_players = 6
    volleyball_players = 2 * tennis_players
    soccer_players = 16 + 22
    total_students = tennis_players + volleyball_players + soccer_players
    result = total_students
    return result

print(solution())