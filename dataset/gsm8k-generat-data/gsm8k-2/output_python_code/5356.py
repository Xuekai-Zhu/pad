def solution():
    """Tom is playing a game and gets 10 points for killing an enemy. If he kills at least 100 enemies he gets a 50% bonus to his score. What was his total score if he killed 150 enemies?"""
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