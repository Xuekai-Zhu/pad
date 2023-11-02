def solution():
    """Carl is taking a class where the whole grade is based on four tests that are graded out of 100. He got an 80, a 75 and a 90 on his first three tests. If he wants an 85 average for the class, what is the minimum grade he needs to get on his last test?"""
    desired_average = 85
    total_points = desired_average * 4
    points_earned = 80 + 75 + 90
    points_needed = total_points - points_earned
    result = points_needed
    return result

print(solution())