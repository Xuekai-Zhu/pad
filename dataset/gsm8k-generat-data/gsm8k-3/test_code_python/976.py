def solution():
    """Ludwig works 7 days a week and he usually works half of the day during Friday, Saturday, and Sunday. If his daily salary is $10, how much does he earn every week?"""
    # Define Ludwig's daily salary and the number of working days
    DAILY_SALARY = 10
    NUM_WORKING_DAYS = 7

    # Calculate Ludwig's earnings for the week
    earnings = (NUM_WORKING_DAYS - 3) * DAILY_SALARY + (DAILY_SALARY / 2) * 3

    # Display Ludwig's earnings
    result = earnings
    return result

print(solution())