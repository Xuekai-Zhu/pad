def solution():
    
    candies_per_hour = 50
    total_candies = 4000
    daily_production = candies_per_hour * 10
    days_to_complete_order = total_candies / daily_production
    result = days_to_complete_order
    return result

print(solution())