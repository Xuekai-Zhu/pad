def solution():
    num_students = 6
    min_fundraising_per_student = 450
    collective_expenses = 3000

    # Calculate the total fundraising goal (6 students * $450 per student + $3000 collective expenses)
    total_goal = num_students * min_fundraising_per_student + collective_expenses

    # Calculate the total amount raised in the first 3 days
    total_raised_first_3_days = 600 + 900 + 400

    # Calculate the total amount raised in the next 4 days (half of the amount raised in the first 3 days)
    total_raised_next_4_days = (600 + 900 + 400) / 2 * 4

    # Calculate the total amount raised in all 7 days
    total_raised = total_raised_first_3_days + total_raised_next_4_days

    # Calculate the total remaining amount needed to reach the goal
    remaining_amount = total_goal - total_raised

    # Calculate the amount each person needs to raise to reach the goal
    amount_per_person = remaining_amount / num_students

    result = amount_per_person
    return result

print(solution())