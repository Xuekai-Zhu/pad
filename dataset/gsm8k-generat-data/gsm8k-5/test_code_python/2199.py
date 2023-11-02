def solution():
    total_students = 1800  # There are 1800 students in total
    foreign_students_pct = 0.3  # 30% of students are foreign

    # Calculate the number of foreign students currently studying
    current_foreign_students = total_students * foreign_students_pct

    # Calculate the total number of foreign students after the new students arrive
    total_foreign_students = current_foreign_students + 200

    result = total_foreign_students
    return result

print(solution())