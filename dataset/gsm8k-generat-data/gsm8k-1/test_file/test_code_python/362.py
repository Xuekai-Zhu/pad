def solution():
    """To be promoted to the next school year, Jane takes 3 tests that together must total at least 42 points. On her first test, Jane scored 15 points, on the second test she scored 18 points. What is the minimum number of points she must score on the third test to pass?"""
    total_points_needed = 42
    points_scored_first_test = 15
    points_scored_second_test = 18
    points_needed_third_test = total_points_needed - points_scored_first_test - points_scored_second_test
    return points_needed_third_test

print(solution())