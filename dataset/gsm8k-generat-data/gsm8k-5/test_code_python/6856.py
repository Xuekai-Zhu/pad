def solution():
    total_students = 600  # Total number of students at River Falls High School
    tennis_players = total_students * (3/4)  # 3/4 of the students play tennis
    both_sports_percentage = 60/100  # 60% of tennis players also play hockey
    both_sports_players = tennis_players * both_sports_percentage  # Number of students who play both sports

    result = both_sports_players
    return result

print(solution())