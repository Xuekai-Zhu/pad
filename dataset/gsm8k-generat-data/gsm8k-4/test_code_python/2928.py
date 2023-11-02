def solution():
    """Oxford High School has 48 teachers, 1 principal and 15 classes with each having 20 students. How many people are there in total in Oxford High School?"""
    # Define the number of teachers, principal, and students in each class
    num_teachers = 48
    num_principal = 1
    num_students_per_class = 20

    # Calculate the total number of students in all classes
    num_students_total = num_students_per_class * 15

    # Calculate the total number of people in the school
    num_people_total = num_teachers + num_principal + num_students_total

    # Return the result
    result = num_people_total
    return result

print(solution())