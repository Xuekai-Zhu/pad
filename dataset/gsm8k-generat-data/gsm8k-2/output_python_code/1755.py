def solution():
    """Madeline needs $1200 to pay rent, $400 for groceries, $200 for medical expenses, and $60 for utilities. She also wants to save $200 in case of an emergency. She makes $15 per hour at her job. How many hours will Madeline need to work this month?"""
    total_expenses = 1200 + 400 + 200 + 60 + 200
    hourly_wage = 15
    hours_needed = total_expenses / hourly_wage
    result = hours_needed
    return result

print(solution())