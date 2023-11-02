def solution():
    weekly_food_budget = 100
    rent = 1500
    video_streaming_services = 30
    cell_phone_usage = 50
    total_monthly_spending = (weekly_food_budget * 4) + rent + video_streaming_services + cell_phone_usage
    savings = total_monthly_spending * 0.1
    result = savings
    return result

print(solution())