def solution():
    """Donny saves $15 on Monday, $28 on Tuesday and $13 on Wednesday. On Thursday he spends half of his total savings so far. How much did he spend?"""
    # Calculate total savings
    total_savings = 15 + 28 + 13

    # Calculate amount spent on Thursday
    spent_on_thursday = total_savings / 2

    # Display amount spent
    result = spent_on_thursday
    return result

print(solution())