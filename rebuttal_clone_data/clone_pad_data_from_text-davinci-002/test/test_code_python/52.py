def solution():
    
    sally_daily_rate = 6
    bob_daily_rate = 4
    days_per_year = 365
    sally_savings = (sally_daily_rate * days_per_year) / 2
    bob_savings = (bob_daily_rate * days_per_year) / 2
    total_savings = sally_savings + bob_savings
    result = total_savings
    return result

print(solution())