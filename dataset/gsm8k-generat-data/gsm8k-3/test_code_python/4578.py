def solution():
    """Grace just started her own business. Each week, she charges 300 dollars. Grace's client will pay her every 2 weeks. How many weeks will it take for Grace to get 1800 dollars?"""
    # Define the weekly charge and the target earnings
    WEEKLY_CHARGE = 300
    TARGET_EARNINGS = 1800

    # Calculate the number of weeks needed to reach the target earnings
    weeks = TARGET_EARNINGS / (WEEKLY_CHARGE * 2)

    # Display the number of weeks
    result = weeks
    return result

print(solution())