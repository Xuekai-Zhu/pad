def solution():
    total_students = 25  # Mr. Bolton's class has 25 students
    math_students = (2/5) * total_students  # 2/5 of the students like maths
    remaining_students = total_students - math_students  # Remaining students who don't like maths
    science_students = (1/3) * remaining_students  # 1/3 of the remaining students like science
    history_students = remaining_students - science_students  # Remaining students like history

    # Calculate the combined total number of students who like history and maths
    total = math_students + history_students
    result = total
    return result

print(solution())