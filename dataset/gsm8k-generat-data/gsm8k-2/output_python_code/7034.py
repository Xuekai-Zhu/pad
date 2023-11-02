def solution():
    """Ahmed and Emily are having a contest to see who can get the best grade in the class. There have been 9 assignments and Ahmed has a 91 in the class. Emily has a 92. The final assignment is worth the same amount as all the other assignments. Emily got a 90 on the final assignment. What is the minimum grade Ahmed needs to get to beat Emily if all grades are whole numbers?"""
    ahmed_average_so_far = 91
    emily_average_so_far = 92
    final_assignment_weight = 1 / 10
    final_assignment_score = 90
    total_weighted_score_ahmed = ahmed_average_so_far * (1 - final_assignment_weight) + final_assignment_score * final_assignment_weight
    minimum_grade_ahmed_can_get = ((emily_average_so_far + 1) - (final_assignment_score * final_assignment_weight)) / (1 - final_assignment_weight)
    result = minimum_grade_ahmed_can_get
    return result

print(solution())