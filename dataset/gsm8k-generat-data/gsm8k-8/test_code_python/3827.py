def solution():
    # Define the total amount of money Jericho has
    total_money = 60 / 2

    # Calculate the amount of money Jericho owes to Manny
    manny_debt = total_money / 2

    # Calculate the total debt Jericho has
    total_debt = 14 + manny_debt

    # Calculate the amount of money Jericho will have left after paying off all debts
    remaining_money = total_money - total_debt
    result = remaining_money
    return result

print(solution())