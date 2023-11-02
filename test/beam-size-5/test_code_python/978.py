def solution():
    
    total_students = 30
    football_players = total_students * 0.2
    remaining_students = total_students - football_players
    cheerleaders = remaining_students * 0.25
    band_players = remaining_students - cheerleaders
    total_early_students = football_players + band_players
    result = total_early_students
    return result

print(solution())