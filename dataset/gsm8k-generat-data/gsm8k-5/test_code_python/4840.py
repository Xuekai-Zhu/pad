def solution():
    donuts_per_dozen = 12  # There are 12 donuts in a dozen
    total_donuts = 4 * donuts_per_dozen  # Noel bakes 4 dozen donuts
    students_in_class = 30  # There are 30 students in the class
    percent_liking_donuts = 0.8  # 80% of the students like donuts

    # Calculate the number of students who like donuts
    students_liking_donuts = int(students_in_class * percent_liking_donuts)

    # Calculate the number of donuts per student who likes donuts
    donuts_per_student = total_donuts / students_liking_donuts
    result = donuts_per_student
    return result

print(solution())