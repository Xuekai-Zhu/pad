def solution():
    num_3pt_goals = 5
    num_2pt_goals = 10
    total_points = 70
    
    # Calculate total points earned from 3-point goals
    three_point_total = num_3pt_goals * 3
    
    # Calculate total points earned from 2-point goals
    two_point_total = num_2pt_goals * 2
    
    # Calculate total points earned by Marcus
    marcus_total = three_point_total + two_point_total
    
    # Calculate percentage of team's total points earned by Marcus
    percent_marcus = (marcus_total / total_points) * 100
    result = percent_marcus
    return result

print(solution())