def solution():
    total_students = 1800
    foreign_percent = 0.3
    new_foreign_students = 200

    # Calculate the current number of foreign students
    current_foreign_students = total_students * foreign_percent

    # Calculate the new number of foreign students after the 200 new students arrive
    new_foreign_students = current_foreign_students + new_foreign_students

    result = new_foreign_students
    return result

print(solution())