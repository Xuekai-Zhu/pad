def solution():
    """Ahmed and Emily are having a contest to see who can get the best grade in the class. There have been 9 assignments and Ahmed has a 91 in the class. Emily has a 92. The final assignment is worth the same amount as all the other assignments. Emily got a 90 on the final assignment. What is the minimum grade Ahmed needs to get to beat Emily if all grades are whole numbers?"""

    # Define Ahmed's and Emily's current total points
    ahmed_points = 91 * 9
    emily_points = 92 * 9

    # Add Emily's points for the final assignment
    emily_points += 90

    # Calculate the minimum grade Ahmed needs to beat Emily
    min_ahmed_grade = (emily_points - ahmed_points + 100) / 10

    # Round up to the nearest whole number
    min_ahmed_grade = int(min_ahmed_grade + 0.5)

    result = min_ahmed_grade
    return result

print(solution())