def solution():
    """At a university there are 1800 students. 30% of all the students are from other countries. Starting next semester, 200 new foreign students will begin studying at this University. How many foreign students will then study at the University if all other students continue to study?"""
    total_students = 1800
    foreign_students_percentage = 0.3
    current_foreign_students = total_students * foreign_students_percentage
    new_foreign_students = 200
    total_foreign_students = current_foreign_students + new_foreign_students
    result = total_foreign_students
    return result

print(solution())