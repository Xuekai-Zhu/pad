def solution():
    """Donny saves $15 on Monday, $28 on Tuesday and $13 on Wednesday. On Thursday he spends half of his total savings so far. How much did he spend?"""
    # Define the money saved on each day
    monday_savings = 15
    tuesday_savings = 28
    wednesday_savings = 13

    # Calculate the total savings so far
    total_savings = monday_savings + tuesday_savings + wednesday_savings

    # Calculate the amount spent on Thursday
    thursday_spending = total_savings / 2

    # Return the result
    result = thursday_spending
    return result

print(solution())