def solution():
    # Calculate the number of students who like donuts
    num_students_like_donuts = round(0.8 * 30)  # 80% of 30 students like donuts

    # Calculate the total number of donuts each student who likes donuts can eat
    total_donuts_available = 4 * 12  # 4 dozen donuts baked
    donuts_per_student = total_donuts_available / num_students_like_donuts

    result = donuts_per_student
    return result

print(solution())