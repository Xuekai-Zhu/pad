def solution():
    """Twice the money Jericho has is 60. He owes Annika $14 and also owes half as much to Manny. After paying off all his debts, how much money will Jericho be left with?"""
    # Calculate the amount of money Jericho has
    jericho_money = 60 / 2

    # Calculate the amount Jericho owes to Manny
    manny_debt = jericho_money / 2

    # Calculate the total amount of debt Jericho has
    total_debt = 14 + manny_debt

    # Calculate the amount of money Jericho will be left with after paying off all his debts
    remaining_money = jericho_money - total_debt

    result = remaining_money
    return result

print(solution())