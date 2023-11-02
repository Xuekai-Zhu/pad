def solution():
    """Mark's basketball team scores 25 2 pointers, 8 3 pointers and 10 free throws. Their opponents score double the 2 pointers but half the 3 pointers and free throws. What's the total number of points scored by both teams added together?"""
    team_2_pointers = 25
    team_3_pointers = 8
    team_free_throws = 10
    team_points = (team_2_pointers * 2) + (team_3_pointers * 3) + team_free_throws
    opponent_2_pointers = 2 * team_2_pointers
    opponent_3_pointers = 0.5 * team_3_pointers
    opponent_free_throws = 0.5 * team_free_throws
    opponent_points = (opponent_2_pointers * 2) + (opponent_3_pointers * 3) + opponent_free_throws
    total_points = team_points + opponent_points
    result = total_points
    return result

print(solution())