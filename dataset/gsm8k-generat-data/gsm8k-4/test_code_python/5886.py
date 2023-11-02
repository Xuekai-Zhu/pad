def solution():
    """At a middle school, 20% of the students are in the band. If 168 students are in the band, how many students go to the middle school?"""
    # Define the percentage of students in the band and the number of students in the band
    percentage_in_band = 20
    students_in_band = 168

    # Calculate the total number of students
    total_students = (students_in_band / percentage_in_band) * 100

    result = int(total_students)
    return result

print(solution())