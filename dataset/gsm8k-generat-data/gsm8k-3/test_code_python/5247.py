def solution():
    """Grant spends $200.00 a year to have the newspaper delivered daily to his house.  Juanita buys the newspaper daily.  Monday through Saturday, she spends $0.50 and on Sunday she spends $2.00.  How much more money does Juanita spend buying the newspaper yearly than Grant?"""
    # Calculate Juanita's weekly newspaper expenses
    weekly_expenses = 6 * 0.5 + 1 * 2
    # Calculate Juanita's yearly newspaper expenses
    yearly_expenses = weekly_expenses * 52
    # Calculate the difference between Juanita's expenses and Grant's expenses
    expense_difference = yearly_expenses - 200
    result = expense_difference
    return result

print(solution())