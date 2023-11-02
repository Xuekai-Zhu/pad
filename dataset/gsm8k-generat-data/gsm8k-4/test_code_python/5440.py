def solution():
    """Each week Jaime saves $50. Every two weeks she spends $46 of her savings on a nice lunch with her mum. How long will it take her to save $135?"""
    # Define Jaime's savings per week and her lunch expense every two weeks
    savings_per_week = 50
    lunch_expense_every_two_weeks = 46

    # Initialize the total savings and the number of weeks
    total_savings = 0
    weeks = 0

    # Keep saving until the total savings reaches $135
    while total_savings < 135:
        # Increment the week counter
        weeks += 1

        # Add the savings for the week
        total_savings += savings_per_week

        # Deduct the lunch expense every two weeks
        if weeks % 2 == 0:
            total_savings -= lunch_expense_every_two_weeks

    result = weeks
    return result

print(solution())