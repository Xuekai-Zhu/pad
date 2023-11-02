def solution():
    """Tom is playing a game and gets 10 points for killing an enemy. If he kills at least 100 enemies he gets a 50% bonus to his score. What was his total score if he killed 150 enemies?"""
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