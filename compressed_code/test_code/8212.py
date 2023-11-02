def solution():
    
    savings_per_week = 25
    weeks_saved = 6
    total_savings = savings_per_week * weeks_saved
    savings_spent = total_savings / 3
    total_savings -= savings_spent
    coat_cost = 170
    money_needed = coat_cost - total_savings
    result = money_needed
    return result

print(solution())