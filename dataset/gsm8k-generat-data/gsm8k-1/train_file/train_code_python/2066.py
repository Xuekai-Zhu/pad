def solution():
    """A group of 6 students organized a fundraiser to go to Nicaragua for the summer. For them to go on the trip, each of them needs at least $450. On top of that, they need $3000 for their miscellaneous collective expenses. On the first day of their fundraiser, they receive $600. On the second day, they receive $900, and on the third day, they receive $400. For the next 4 days, they receive only half of what they raised on the first 3 days. How much more money does each person need to raise for them to reach their goal?"""
    num_students = 6
    min_fund = 450
    misc_expenses = 3000
    total_goal = num_students * min_fund + misc_expenses
    
    first_three_days = 600 + 900 + 400
    next_four_days = (first_three_days / 2) * 4
    total_raised = first_three_days + next_four_days
    
    remaining_fund = total_goal - total_raised
    per_person_fund = remaining_fund / num_students
    
    result = per_person_fund
    return result

print(solution())