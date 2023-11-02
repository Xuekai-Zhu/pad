def solution():
    """Vanessa wants to buy a dress she saw at the mall, which costs $80, and she already has $20 in savings. Her parents give her $30 every week, but she also spends $10 each weekend at the arcades. How many weeks will she have to wait until she can gather enough money to buy the dress?"""
    
    # Define the cost of the dress, savings, weekly allowance, and weekly arcade spending
    DRESS_COST = 80
    SAVINGS = 20
    WEEKLY_ALLOWANCE = 30
    WEEKLY_ARCADE_SPENDING = 10

    # Calculate the amount of money Vanessa will have after each week
    total_money = SAVINGS
    weeks = 0
    while total_money < DRESS_COST:
        total_money += WEEKLY_ALLOWANCE - WEEKLY_ARCADE_SPENDING
        weeks += 1

    # Display the number of weeks Vanessa has to wait
    result = weeks
    return result

print(solution())