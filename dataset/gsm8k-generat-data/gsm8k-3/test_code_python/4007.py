def solution():
    """Liz's basketball team is down by 20 points in the final quarter of their game.  Liz goes on a shooting spree, sinking 5 free throw shots, 3 three-pointers, and 4 other jump shots.  The other team only scores 10 points that quarter, and none of Liz's teammates manage to score any points.  How much does Liz's team lose by at the end of the game?"""
    # Define the number of points for each type of shot
    FREE_THROW_POINTS = 1
    THREE_POINTER_POINTS = 3
    JUMP_SHOT_POINTS = 2

    # Calculate the number of points Liz scores
    free_throw_points = 5 * FREE_THROW_POINTS
    three_pointer_points = 3 * THREE_POINTER_POINTS
    jump_shot_points = 4 * JUMP_SHOT_POINTS
    liz_points = free_throw_points + three_pointer_points + jump_shot_points

    # Calculate the number of points the other team scores
    other_team_points = 10

    # Calculate the final score difference
    score_difference = other_team_points - liz_points - 20

    # Display the score difference
    result = score_difference
    return result

print(solution())