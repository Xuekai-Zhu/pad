def solution():
    """Celia is creating a budget for the next 4 weeks. She wants to spend no more than $100 a week on food. For rent for her apartment, she plans to spend $1500. She has $30 set aside for video streaming services for the month. She also has $50 planned for one month of cell phone usage. After she adds up all of her spending for the month she wants to set aside 10% of it to put into savings. How much money is Celia going to put into her savings account?"""
    # Define the weekly budget for food and the monthly expenses
    weekly_food_budget = 100
    rent = 1500
    video_streaming = 30
    cell_phone = 50

    # Calculate the total monthly expenses
    total_expenses = (weekly_food_budget * 4) + rent + video_streaming + cell_phone

    # Calculate the amount to put into savings
    savings = total_expenses * 0.1

    result = savings
    return result

print(solution())