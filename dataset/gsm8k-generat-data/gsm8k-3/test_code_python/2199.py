def solution():
    """At a university there are 1800 students. 30% of all the students are from other countries. Starting next semester, 200 new foreign students will begin studying at this University. How many foreign students will then study at the University if all other students continue to study?"""
    # Define the total number of students and the percentage of foreign students
    total_students = 1800
    foreign_percentage = 0.3

    # Calculate the current number of foreign students
    current_foreign_students = int(total_students * foreign_percentage)

    # Calculate the total number of foreign students after the new students arrive
    total_foreign_students = current_foreign_students + 200

    # Display the total number of foreign students
    result = total_foreign_students
    return result

print(solution())