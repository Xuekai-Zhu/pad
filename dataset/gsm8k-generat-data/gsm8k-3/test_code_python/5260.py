def solution():
    """Celia is creating a budget for the next 4 weeks. She wants to spend no more than $100 a week on food. For rent for her apartment, she plans to spend $1500. She has $30 set aside for video streaming services for the month. She also has $50 planned for one month of cell phone usage. After she adds up all of her spending for the month she wants to set aside 10% of it to put into savings. How much money is Celia going to put into her savings account?"""
    # Define the variable values
    WEEKLY_FOOD_BUDGET = 100
    RENT = 1500
    VIDEO_STREAMING = 30
    CELL_PHONE = 50

    # Calculate the total spending
    total_spending = (WEEKLY_FOOD_BUDGET*4) + RENT + VIDEO_STREAMING + CELL_PHONE

    # Calculate the amount to put into savings
    savings = total_spending * 0.1

    # Display the amount to put into savings
    result = savings
    return result

print(solution())