def solution():
    """John puts $25 in his piggy bank every month for 2 years to save up for a vacation. He had to spend $400 from his piggy bank savings last week to repair his car. How many dollars are left in his piggy bank?"""
    months = 2
    savings_per_month = 25
    total_saved = months * savings_per_month
    spent = 400
    remaining = total_saved - spent
    result = remaining
    return result

print(solution())