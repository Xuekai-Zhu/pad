def solution():
    num_students = 6
    min_personal_fund = 450
    misc_expenses = 3000

    # Calculate the total amount needed for the trip
    total_fund_needed = (min_personal_fund * num_students) + misc_expenses

    # Calculate the total amount raised on the first 3 days
    total_raised_first_3_days = 600 + 900 + 400

    # Calculate the total amount raised on the next 4 days
    total_raised_next_4_days = (total_raised_first_3_days / 2) * 4

    # Calculate the total amount raised in the entire fundraiser
    total_raised = total_raised_first_3_days + total_raised_next_4_days

    # Calculate how much more money each person needs to raise
    remaining_amount = total_fund_needed - total_raised
    per_person_remaining = remaining_amount / num_students
    result = per_person_remaining
    return result

print(solution())