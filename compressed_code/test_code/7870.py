def solution():
    
    john_old_rent = 1200
    new_rent_increase_percent = 40
    new_rent = john_old_rent * (1 + new_rent_increase_percent / 100)
    total_rent = new_rent / 3
    john_savings_per_month = john_old_rent - total_rent
    john_savings_per_year = john_savings_per_month * 12
    
    result = john_savings_per_year
    return result

print(solution())