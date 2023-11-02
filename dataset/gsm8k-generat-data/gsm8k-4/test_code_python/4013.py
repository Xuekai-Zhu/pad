def solution():
    """Kate saved $27 in March. She saved $13 in April and $28 in May. Then Kate spent $49 on a keyboard and $5 on a mouse. How much money does Kate have left?"""
    # Define the amounts saved in the different months
    march_savings = 27
    april_savings = 13
    may_savings = 28

    # Calculate the total savings
    total_savings = march_savings + april_savings + may_savings

    # Define the amount spent on the keyboard and mouse
    spending = 49 + 5

    # Calculate the amount of money Kate has left
    remaining_money = total_savings - spending

    result = remaining_money
    return result

print(solution())