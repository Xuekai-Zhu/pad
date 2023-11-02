def solution():
    """Tom is playing a game and gets 10 points for killing an enemy.  If he kills at least 100 enemies he gets a 50% bonus to his score.  What was his total score if he killed 150 enemies?"""
    # Define the base point value per enemy killed
    BASE_POINTS = 10

    # Define the number of enemies killed
    enemies_killed = 150

    # Calculate the total points earned without bonus
    base_points_earned = enemies_killed * BASE_POINTS

    # Calculate the bonus points earned if enemies killed is at least 100
    bonus_points_earned = 0
    if enemies_killed >= 100:
        bonus_points_earned = base_points_earned * 0.5

    # Calculate the total points earned with bonus
    total_points_earned = base_points_earned + bonus_points_earned

    # Display the total points earned
    result = total_points_earned
    return result

print(solution())