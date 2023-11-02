def solution():
    """At a school, 40% of the students receive a free lunch. These lunches are paid for by making sure the price paid by the paying students is enough to cover everyone's meal. If it costs $210 to feed 50 students, how much do the paying students pay for lunch?"""
    # Define the total number of students and the percentage of students receiving a free lunch
    total_students = 50
    free_lunch_percentage = 0.4

    # Calculate the number of students receiving a free lunch and the number of paying students
    free_lunch_students = total_students * free_lunch_percentage
    paying_students = total_students - free_lunch_students

    # Calculate the cost per paying student
    cost_per_paying_student = 210 / paying_students

    # Return the cost per paying student rounded to 2 decimal places
    result = round(cost_per_paying_student, 2)
    return result

print(solution())