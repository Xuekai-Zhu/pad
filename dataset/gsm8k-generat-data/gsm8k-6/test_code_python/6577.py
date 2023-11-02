def solution():
    # Calculate the total points Jimmy earned in the exams
    total_exam_points = 20 * 3
    
    # Calculate the total points Jimmy has after losing 5 points for bad behavior
    total_points = total_exam_points - 5
    
    # Calculate the minimum number of points Jimmy needs to pass to the next class
    minimum_passing_points = 50
    
    # Calculate the number of points Jimmy can still lose and pass to the next class
    points_can_lose = minimum_passing_points - total_points
    
    result = points_can_lose
    return result

print(solution())