def solution():
    """Ahmed and Emily are having a contest to see who can get the best grade in the class. There have been 9 assignments and Ahmed has a 91 in the class. Emily has a 92. The final assignment is worth the same amount as all the other assignments. Emily got a 90 on the final assignment. What is the minimum grade Ahmed needs to get to beat Emily if all grades are whole numbers?"""
    # Define Ahmed and Emily's scores
    ahmed_score = 91
    emily_score = 92

    # Calculate the total points for all assignments except the final
    total_points_except_final = 9 * 100

    # Subtract Emily's score from the total points to find the minimum score Ahmed needs to beat her
    # and round up to the nearest integer
    min_ahmed_score = int((total_points_except_final + 90 + emily_score) - ahmed_score + 0.5)

    result = min_ahmed_score
    return result

print(solution())