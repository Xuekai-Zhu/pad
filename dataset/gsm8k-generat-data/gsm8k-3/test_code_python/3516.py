def solution():
    """In one of the teacher's meetings, it was agreed that each class will contribute $90 for a school activity. The class of Miss Evans has $14 class funds and they decided to use it to lessen the contribution of each student. If the remaining amount will be divided among 19 students, how much will each student contribute?"""
    # Define the total contribution needed and the number of students
    total_contribution = 90
    num_students = 19

    # Define the amount of class funds available
    class_funds = 14

    # Calculate the total amount of money available for dividing among students
    total_money = (total_contribution * num_students) - class_funds

    # Calculate the amount each student will contribute
    student_contribution = total_money / num_students

    # Display the amount each student will contribute
    result = student_contribution
    return result

print(solution())