def solution():
    
    food_budget_per_week = 100
    rent_per_month = 1500
    video_streaming_budget_per_month = 30
    cell_phone_budget_per_month = 50
    total_food_budget = food_budget_per_week * 4
    total_budget = total_food_budget + rent_per_month + video_streaming_budget_per_month + cell_phone_budget_per_month
    savings_amount = total_budget * 0.1
    result = savings_amount
    return result

print(solution())