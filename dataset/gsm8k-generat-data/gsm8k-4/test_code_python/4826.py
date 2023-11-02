def solution():
    """Tyson played basketball on the schoolyard. He scored three points fifteen times, and two points twelve times. He also scored one point some number of times. How many times did he score one point, if in total he scored 75 points?"""
    # Define the number of times Tyson scored three points and two points
    three_points = 15
    two_points = 12
    
    # Calculate the total points from three-point shots and two-point shots
    total_points = 3*three_points + 2*two_points
    
    # Calculate the number of points Tyson scored with one-point shots
    one_points = (75 - total_points) / 1
    
    result = one_points
    return result

print(solution())