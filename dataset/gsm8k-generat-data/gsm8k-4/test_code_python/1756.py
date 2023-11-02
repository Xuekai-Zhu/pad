def solution():
    """Madeline needs $1200 to pay rent, $400 for groceries, $200 for medical expenses, and $60 for utilities. She also wants to save $200 in case of an emergency. She makes $15 per hour at her job. How many hours will Madeline need to work this month?"""
    # Calculate the total amount of expenses
    total_expenses = 1200 + 400 + 200 + 60 + 200

    # Calculate the required income after savings
    required_income = total_expenses / 0.75

    # Calculate the required hours of work
    required_hours = required_income / 15

    # Round up the required hours to the nearest integer
    required_hours = int(math.ceil(required_hours))

    result = required_hours
    return result

print(solution())