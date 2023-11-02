def solution():
    """Celia is creating a budget for the next 4 weeks. She wants to spend no more than $100 a week on food. For rent for her apartment, she plans to spend $1500. She has $30 set aside for video streaming services for the month. She also has $50 planned for one month of cell phone usage. After she adds up all of her spending for the month she wants to set aside 10% of it to put into savings. How much money is Celia going to put into her savings account?"""
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