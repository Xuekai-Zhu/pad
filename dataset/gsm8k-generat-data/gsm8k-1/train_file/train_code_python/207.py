def solution():
    """John puts $25 in his piggy bank every month for 2 years to save up for a vacation. He had to spend $400 from his piggy bank savings last week to repair his car. How many dollars are left in his piggy bank?"""
    savings_per_month = 25
    total_months_saved = 2 * 12
    total_savings = savings_per_month * total_months_saved
    spending = 400
    remaining_savings = total_savings - spending
    result = remaining_savings
    return result

print(solution())