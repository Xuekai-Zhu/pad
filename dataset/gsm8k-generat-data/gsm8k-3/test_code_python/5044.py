def solution():
    """At Rainbow Preschool, there are 80 students.  25% of them are half-day students and get picked up at noon, while the rest are full-day students. How many are full-day students?"""
    # Define the total number of students and the percentage of half-day students
    total_students = 80
    half_day_percentage = 0.25

    # Calculate the number of half-day students and full-day students
    half_day_students = total_students * half_day_percentage
    full_day_students = total_students - half_day_students

    # Display the number of full-day students
    result = full_day_students
    return result

print(solution())