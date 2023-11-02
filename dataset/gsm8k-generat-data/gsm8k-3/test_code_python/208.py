def solution():
    """John puts $25 in his piggy bank every month for 2 years to save up for a vacation. He had to spend $400 from his piggy bank savings last week to repair his car. How many dollars are left in his piggy bank?"""
    # Define the amount saved each month for 2 years
    monthly_savings = 25
    total_savings = monthly_savings * 24

    # Subtract the amount spent on car repair
    remaining_savings = total_savings - 400

    # return the result
    result = remaining_savings
    return result

print(solution())