def solution():
    """A group of 6 students organized a fundraiser to go to Nicaragua for the summer. For them to go on the trip, each of them needs at least $450. On top of that, they need $3000 for their miscellaneous collective expenses. On the first day of their fundraiser, they receive $600. On the second day, they receive $900, and on the third day, they receive $400. For the next 4 days, they receive only half of what they raised on the first 3 days. How much more money does each person need to raise for them to reach their goal?"""
    num_students = 6
    min_cost_per_student = 450
    miscellaneous_expenses = 3000
    total_cost = (min_cost_per_student * num_students) + miscellaneous_expenses
    total_raised = 600 + 900 + 400
    for i in range(4):
        total_raised += (0.5 * total_raised)
    remaining_cost = total_cost - total_raised
    remaining_per_student = remaining_cost / num_students
    result = round(remaining_per_student, 2)
    return result

print(solution())