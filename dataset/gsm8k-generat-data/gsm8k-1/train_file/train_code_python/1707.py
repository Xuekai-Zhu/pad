def solution():
    """Mark's basketball team scores 25 2 pointers, 8 3 pointers and 10 free throws. Their opponents score double the 2 pointers but half the 3 pointers and free throws. What's the total number of points scored by both teams added together?"""
    team_points = (25*2) + (8*3) + 10
    opponent_2pt = 2 * 25
    opponent_3pt = 0.5 * 8 * 3
    opponent_ft = 0.5 * 10
    opponent_points = opponent_2pt + opponent_3pt + opponent_ft
    total_points = team_points + opponent_points
    result = total_points
    return result

print(solution())