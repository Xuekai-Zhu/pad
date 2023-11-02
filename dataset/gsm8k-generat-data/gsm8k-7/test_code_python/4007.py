def solution():
    points_from_free_throws = 5
    points_from_three_pointers = 3 * 3
    points_from_jump_shots = 4 * 2
    points_scored_by_opponents = 10
    point_deficit_before_Liz_started_scoring = 20
    
    # Calculate the total points scored by Liz's team in the final quarter
    total_points_scored_by_Liz = points_from_free_throws + points_from_three_pointers + points_from_jump_shots
    
    # Calculate the final point deficit after Liz's scoring spree
    final_point_deficit = point_deficit_before_Liz_started_scoring - total_points_scored_by_Liz + points_scored_by_opponents
    result = final_point_deficit
    return result

print(solution())