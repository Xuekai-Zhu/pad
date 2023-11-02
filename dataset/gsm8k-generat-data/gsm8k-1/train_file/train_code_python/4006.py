def solution():
    """Liz's basketball team is down by 20 points in the final quarter of their game. Liz goes on a shooting spree, sinking 5 free throw shots, 3 three-pointers, and 4 other jump shots. The other team only scores 10 points that quarter, and none of Liz's teammates manage to score any points. How much does Liz's team lose by at the end of the game?"""
    starting_deficit = 20
    free_throws = 5
    three_pointers = 3
    jump_shots = 4
    total_points_scored = (free_throws * 1) + (three_pointers * 3) + (jump_shots * 2)
    points_allowed = 10
    final_deficit = starting_deficit + total_points_scored - points_allowed
    result = final_deficit
    return result

print(solution())