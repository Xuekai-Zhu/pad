def solution():
    """Vanessa wants to buy a dress she saw at the mall, which costs $80, and she already has $20 in savings. Her parents give her $30 every week, but she also spends $10 each weekend at the arcades. How many weeks will she have to wait until she can gather enough money to buy the dress?"""
    # Define the cost of the dress and Vanessa's initial savings
    cost = 80
    savings = 20

    # Define Vanessa's weekly income and expenses
    income = 30
    expenses = 10

    # Initialize the number of weeks Vanessa needs to save
    weeks = 0

    # Calculate Vanessa's savings each week until she has enough to buy the dress
    while savings < cost:
        # Increment the number of weeks
        weeks += 1

        # Add Vanessa's income and subtract her expenses
        savings += income - expenses

    # Return the number of weeks it took for Vanessa to save enough money
    result = weeks
    return result

print(solution())