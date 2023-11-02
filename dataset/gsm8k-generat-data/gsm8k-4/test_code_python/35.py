def solution():
    """Mr. Sanchez found out that 40% of his Grade 5  students got a final grade below B. How many of his students got a final grade of B and above if he has 60 students in Grade 5?"""
    # Define the total number of students
    total_students = 60

    # Calculate the number of students who got a final grade below B
    below_b_students = total_students * 0.4

    # Calculate the number of students who got a final grade of B and above
    above_b_students = total_students - below_b_students

    # return the result
    result = above_b_students
    return result

print(solution())