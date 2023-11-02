def solution():
    """Grace just started her own business. Each week, she charges 300 dollars. Grace's client will pay her every 2 weeks. How many weeks will it take for Grace to get 1800 dollars?"""
    # Define the amount Grace charges per week
    weekly_charge = 300

    # Define the target earnings
    target_earnings = 1800

    # Calculate the number of weeks it will take to reach the target earnings
    weeks = target_earnings / (weekly_charge * 2)

    # return the result
    result = weeks
    return result

print(solution())