def solution():
    price_per_kg = 20
    past_four_months = 80
    today = past_four_months * 2
    
    total_fish = past_four_months + today
    
    total_earnings = total_fish * price_per_kg
    
    result = total_earnings
    return result

print(solution())