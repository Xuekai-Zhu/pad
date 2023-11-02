def solution():
    """Peter has a plan to take his family on a vacation to Germany. He needs $5,000 to cover all the spending for the travel, and he has $2,900 in savings right now. If he can save up $700 each month, how many months does he need to wait to reach his goal?"""
    total_cost = 5000
    current_savings = 2900
    monthly_savings = 700
    months_needed = (total_cost - current_savings) / monthly_savings
    result = months_needed
    return result

print(solution())