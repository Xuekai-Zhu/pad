def solution():
    """There are 10 students in a class. The average age of 9 of them is 8 years. By how many years will this average increase if the tenth student is (quite strangely) 28 years old?"""
    # Define the number of students, the current average age, and the age of the 10th student
    num_students = 10
    current_avg_age = 8
    tenth_student_age = 28

    # Calculate the total age of the 9 students
    total_age = current_avg_age * (num_students - 1)

    # Add the age of the 10th student
    total_age += tenth_student_age

    # Calculate the new average age of all 10 students
    new_avg_age = total_age / num_students

    # Calculate the increase in the average age
    increase = new_avg_age - current_avg_age

    # return the result
    result = increase
    return result

print(solution())