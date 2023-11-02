def solution():
    points_per_enemy = 10
    enemy_threshold_for_bonus = 100
    bonus_percentage = 0.5
    total_enemies_killed = 150

    # Calculate the base score for killing enemies
    base_score = points_per_enemy * total_enemies_killed

    # Apply bonus if the threshold is met or exceeded
    if total_enemies_killed >= enemy_threshold_for_bonus:
        bonus_score = base_score * bonus_percentage
        total_score = base_score + bonus_score
    else:
        total_score = base_score

    result = total_score
    return result

print(solution())