def solution():
    """Madeline needs $1200 to pay rent, $400 for groceries, $200 for medical expenses, and $60 for utilities. She also wants to save $200 in case of an emergency. She makes $15 per hour at her job. How many hours will Madeline need to work this month?"""
    # Calculate the total expenses
    total_expenses = 1200 + 400 + 200 + 60 + 200

    # Calculate the total amount of money Madeline needs to earn
    total_earnings = total_expenses / (1 - 0.3)  # 30% of earnings is for taxes

    # Calculate the number of hours Madeline needs to work
    hours_needed = total_earnings / 15  # Madeline makes $15 per hour

    # Display the number of hours Madeline needs to work
    result = hours_needed
    return result

print(solution())