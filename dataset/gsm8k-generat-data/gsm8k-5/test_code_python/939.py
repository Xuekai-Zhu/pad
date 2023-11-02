def solution():
    total_students = 20 # There are 20 students in the class
    basketball_players = total_students / 2 # Half of the students play basketball
    volleyball_players = total_students * 2 / 5 # Two-fifths of the students play volleyball
    basketball_and_volleyball_players = total_students / 10 # One-tenth of the students play both games

    # Calculate the number of students who do not play either game
    non_players = total_students - (basketball_players + volleyball_players - basketball_and_volleyball_players)
    result = non_players
    return result

print(solution())