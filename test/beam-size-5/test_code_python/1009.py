def solution():
    
    wages_per_week = 10
    tips_per_week = 15
    total_wages = wages_per_week * 40
    total_tips = tips_per_week * 40
    total_cost = 10000
    savings_percentage = 0.2
    weeks_to_save = (total_cost - total_wages) / savings_percentage
    result = weeks_to_save
    return result

print(solution())