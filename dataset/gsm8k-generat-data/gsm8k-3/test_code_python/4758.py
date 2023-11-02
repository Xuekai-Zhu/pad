def solution():
    """At a school, 40% of the students receive a free lunch. These lunches are paid for by making sure the price paid by the paying students is enough to cover everyone's meal. If it costs $210 to feed 50 students, how much do the paying students pay for lunch?"""
    
    # Define the percentage of students who pay for lunch
    paying_percent = 100 - 40

    # Calculate the number of paying students
    paying_students = 50 * paying_percent / 100

    # Calculate the cost per paying student
    cost_per_paying_student = 210 / paying_students

    # Display the cost per paying student
    result = cost_per_paying_student
    return result

print(solution())