def solution():
    """Ahmed and Emily are having a contest to see who can get the best grade in the class. There have been 9 assignments and Ahmed has a 91 in the class. Emily has a 92. The final assignment is worth the same amount as all the other assignments. Emily got a 90 on the final assignment. What is the minimum grade Ahmed needs to get to beat Emily if all grades are whole numbers?"""
    total_possible_points = 9 * 100
    ahmed_total_points = 9 * 91
    emily_total_points = (8 * 92) + 90
    min_grade_ahmed = ((emily_total_points + 1) - ahmed_total_points) / 100
    result = int(min_grade_ahmed)
    return result

print(solution())