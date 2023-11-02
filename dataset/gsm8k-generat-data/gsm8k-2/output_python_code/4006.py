def solution():
    """Liz's basketball team is down by 20 points in the final quarter of their game. Liz goes on a shooting spree, sinking 5 free throw shots, 3 three-pointers, and 4 other jump shots. The other team only scores 10 points that quarter, and none of Liz's teammates manage to score any points. How much does Liz's team lose by at the end of the game?"""
    free_throw_points = 1
    three_point_points = 3
    jump_shot_points = 2
    liz_points = (5 * free_throw_points) + (3 * three_point_points) + (4 * jump_shot_points)
    opposing_team_points = 10
    final_score_difference = 20 - (liz_points - opposing_team_points)
    result = final_score_difference
    return result

print(solution())