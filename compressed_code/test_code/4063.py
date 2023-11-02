def solution():
    
    food_weekly = 100
    rent_monthly = 1500
    streaming_services = 30
    cell_phone = 50
    total_spending = (food_weekly * 4) + rent_monthly + streaming_services + cell_phone
    savings = total_spending * 0.10
    result = savings
    return result

print(solution())