def solution():
    
    total_games = 20
    first_year_attended = int(total_games * 0.9)
    second_year_attended = first_year_attended - 4
    result = second_year_attended
    return result

print(solution())