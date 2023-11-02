def solution():
    """There are 19 students in the 3rd grade and twice that number in the 4th grade. There are 10 boys and 19 girls in the 2nd grade. How many students are there in total?"""
    # Define the number of students in each grade
    grade3_students = 19
    grade4_students = grade3_students * 2
    grade2_students = 10 + 19

    # Calculate the total number of students
    total_students = grade3_students + grade4_students + grade2_students

    # Display the total number of students
    result = total_students
    return result

print(solution())