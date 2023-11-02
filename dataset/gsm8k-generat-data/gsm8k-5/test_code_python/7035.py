def solution():
    total_points = 9 * 100  # There are 9 assignments and each is worth 100 points
    ahmed_points = 91 * 9  # Ahmed has a 91 in the class so far, so he has earned 91 points on each assignment
    emily_points = 92 * 9 + 90  # Emily has a 92 in the class so far and got a 90 on the final assignment

    # Calculate the minimum grade Ahmed needs to beat Emily
    required_ahmed_grade = (emily_points - ahmed_points) / 10
    result = required_ahmed_grade
    return result

print(solution())