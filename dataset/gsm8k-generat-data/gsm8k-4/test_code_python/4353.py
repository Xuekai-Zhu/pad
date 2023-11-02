def solution():
    """Norris saved $29 in September. He saved $25 in October and $31 in November. Then Hugo spent $75 on an online game. How much money does Norris have left?"""
    # Define the amount of money saved in each month
    september_savings = 29
    october_savings = 25
    november_savings = 31

    # Calculate the total savings
    total_savings = september_savings + october_savings + november_savings

    # Subtract the amount spent by Hugo
    remaining_money = total_savings - 75

    # Return the result
    result = remaining_money
    return result

print(solution())