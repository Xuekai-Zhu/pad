def solution():
    
    points_per_enemy = 10
    total_enemies = 150
    bonus_enemies = 100
    bonus_percentage = 0.5

    base_score = points_per_enemy * total_enemies
    bonus_score = 0
    if total_enemies >= bonus_enemies:
        bonus_score = base_score * bonus_percentage
    
    total_score = base_score + bonus_score
    result = total_score
    return result

print(solution())