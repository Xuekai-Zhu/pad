def solution():
    grades = 4  # Cedar Falls Middle School has 4 grades
    grades_per_year = 7  # There are 7 grades in each grade
    students_per_grade = 10  # There are 10 students in each grade
    points_per_grade = points_per_grade / 8  # There are 8 points in each grade
    total_points = grades_per_year * students_per_grade * points_per_grade  # Calculate the total points needed for the escape room

    # Calculate the time it will take for everyone to try the escape room
    time_per_group = 45 / total_points  # Calculate the time it will take for everyone to try the escape room
    result = time_per_group
    return result

print(solution())