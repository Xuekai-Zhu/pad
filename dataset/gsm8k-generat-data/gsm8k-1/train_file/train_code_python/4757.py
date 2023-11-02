def solution():
    """At a school, 40% of the students receive a free lunch. These lunches are paid for by making sure the price paid by the paying students is enough to cover everyone's meal. If it costs $210 to feed 50 students, how much do the paying students pay for lunch?"""
    total_students = 50
    free_lunch_students = 0.4 * total_students
    paying_students = total_students - free_lunch_students
    cost_per_paying_student = 210 / paying_students
    result = cost_per_paying_student
    return result

print(solution())