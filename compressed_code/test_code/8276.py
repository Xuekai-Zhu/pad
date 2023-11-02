def solution():
    
    current_value = 90
    investment = current_value / 3
    months = 5
    earned = current_value - investment
    earnings_per_month = earned / months
    result = earnings_per_month
    return result

print(solution())