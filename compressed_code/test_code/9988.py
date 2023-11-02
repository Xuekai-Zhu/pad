def solution():
    
    points_per_enemy = 10
    enemy_count = 150
    base_score = enemy_count * points_per_enemy
    if enemy_count >= 100:
        bonus_score = base_score * 0.5
        total_score = base_score + bonus_score
    else:
        total_score = base_score
    result = total_score
    return result

print(solution())