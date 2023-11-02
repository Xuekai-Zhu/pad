def solution():
    num_enemies = 150
    points_per_enemy = 10
    bonus_threshold = 100
    bonus_percentage = 0.5

    # Calculate Tom's base score
    base_score = num_enemies * points_per_enemy

    # If Tom killed enough enemies, apply the bonus
    if num_enemies >= bonus_threshold:
        bonus = base_score * bonus_percentage
        total_score = base_score + bonus
    else:
        total_score = base_score

    result = total_score
    return result

print(solution())