def solution():
    """At Rainbow Preschool, there are 80 students. 25% of them are half-day students and get picked up at noon, while the rest are full-day students. How many are full-day students?"""
    # Define the total number of students
    total_students = 80

    # Calculate the number of half-day students
    halfday_students = total_students * 0.25

    # Calculate the number of full-day students
    fullday_students = total_students - halfday_students

    # Return the result
    result = fullday_students
    return result

print(solution())