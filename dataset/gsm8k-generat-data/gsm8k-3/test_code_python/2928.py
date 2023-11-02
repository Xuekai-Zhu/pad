def solution():
    """Oxford High School has 48 teachers, 1 principal and 15 classes with each having 20 students. How many people are there in total in Oxford High School?"""
    # Define the number of teachers, principal, and students per class
    NUM_TEACHERS = 48
    NUM_PRINCIPAL = 1
    NUM_STUDENTS_PER_CLASS = 20

    # Calculate the total number of students
    num_students = NUM_STUDENTS_PER_CLASS * 15

    # Calculate the total number of people in the school
    total_people = NUM_TEACHERS + NUM_PRINCIPAL + num_students

    # Display the total number of people
    result = total_people
    return result

print(solution())