def solution():
    # Calculate Mark's team's total points
    total_points = (25*2) + (8*3) + 10 # 25 2-pointers, 8 3-pointers, and 10 free throws
    
    # Calculate the opponent's total points
    opp_2_pointers = 2 * 25  # double the 2-pointers
    opp_3_pointers = (1/2) * 8 * 3  # half the 3-pointers
    opp_free_throws = (1/2) * 10  # half the free throws
    opp_total_points = opp_2_pointers + opp_3_pointers + opp_free_throws
    
    # Calculate the total points scored by both teams
    total_points_scored = total_points + opp_total_points
    
    result = total_points_scored
    return result

print(solution())