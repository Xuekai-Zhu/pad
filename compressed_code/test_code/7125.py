def solution():
    
    total_games = 20
    attended_first_year = int(total_games * 0.9)
    attended_second_year = attended_first_year - 4
    result = attended_second_year
    return result

print(solution())