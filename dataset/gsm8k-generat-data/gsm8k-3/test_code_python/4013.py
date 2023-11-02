def solution():
    """Kate saved $27 in March. She saved $13 in April and $28 in May. Then Kate spent $49 on a keyboard and $5 on a mouse. How much money does Kate have left?"""
    # Define the amounts saved in each month
    march_savings = 27
    april_savings = 13
    may_savings = 28

    # Calculate the total savings
    total_savings = march_savings + april_savings + may_savings

    # Define the amounts spent
    keyboard_cost = 49
    mouse_cost = 5

    # Calculate the total amount spent
    total_spent = keyboard_cost + mouse_cost

    # Calculate the remaining amount of money
    remaining_money = total_savings - total_spent

    # Display the remaining amount of money
    result = remaining_money
    return result

print(solution())