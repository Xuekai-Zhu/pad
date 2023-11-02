def solution():
    # Calculate the total points Ahmed has earned on the first 9 assignments
    ahmed_points = 91 * 9

    # Calculate the minimum total points Ahmed needs to beat Emily
    emily_points = 92 * 9 + 90
    min_ahmed_points = emily_points - ahmed_points

    # Calculate the minimum grade Ahmed needs to get on the final assignment to beat Emily
    min_ahmed_grade = (min_ahmed_points + 9) // 10

    result = min_ahmed_grade
    return result

print(solution())