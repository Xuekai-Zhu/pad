def solution():
    """Celia is creating a budget for the next 4 weeks. She wants to spend no more than $100 a week on food. For rent for her apartment, she plans to spend $1500. She has $30 set aside for video streaming services for the month. She also has $50 planned for one month of cell phone usage. After she adds up all of her spending for the month she wants to set aside 10% of it to put into savings. How much money is Celia going to put into her savings account?"""
    food_weekly = 100
    rent_monthly = 1500
    streaming_services = 30
    cell_phone = 50
    total_spending = (food_weekly * 4) + rent_monthly + streaming_services + cell_phone
    savings = total_spending * 0.10
    result = savings
    return result

print(solution())