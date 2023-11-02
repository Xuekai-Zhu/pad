def solution():
    """Tom is playing a game and gets 10 points for killing an enemy. If he kills at least 100 enemies he gets a 50% bonus to his score. What was his total score if he killed 150 enemies?"""
    # Define the number of enemies killed and the base score per enemy
    enemies_killed = 150
    base_score = 10

    # Calculate the total score without bonus
    total_score = enemies_killed * base_score

    # Add the bonus if applicable
    if enemies_killed >= 100:
        bonus = 0.5 * total_score
        total_score += bonus

    result = total_score
    return result

print(solution())