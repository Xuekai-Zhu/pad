def solution():
    total_students = 600
    tennis_players_ratio = 0.75

    # Calculate the number of students who play tennis
    tennis_players = total_students * tennis_players_ratio

    # Calculate the number of students who play both hockey and tennis
    hockey_and_tennis_players = tennis_players * 0.6

    result = hockey_and_tennis_players
    return result

print(solution())