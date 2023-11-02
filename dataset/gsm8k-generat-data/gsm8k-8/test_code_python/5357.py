def solution():
    # Define the points per kill and the number of enemies killed
    points_per_kill = 10
    num_enemies_killed = 150

    # Calculate the base score and the bonus score
    base_score = points_per_kill * num_enemies_killed
    bonus_score = 0
    if num_enemies_killed >= 100:
        bonus_score = 0.5 * base_score

    # Calculate the total score
    total_score = base_score + bonus_score
    result = total_score
    return result

print(solution())