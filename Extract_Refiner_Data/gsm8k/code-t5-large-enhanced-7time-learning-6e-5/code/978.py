def solution():
    
    total_students = 30
    football_players = total_students * 0.2
    remaining_students = total_students - football_players
    cheerleaders = remaining_students * 0.25
    early_leavers = (remaining_students - cheerleaders) * 3
    result = early_leavers
    return result

print(solution())