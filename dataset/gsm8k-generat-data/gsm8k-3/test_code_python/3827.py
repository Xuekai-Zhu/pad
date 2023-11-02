def solution():
    """Twice the money Jericho has is 60. He owes Annika $14 and also owes half as much to Manny. After paying off all his debts, how much money will Jericho be left with?"""
    # Calculate how much money Jericho has
    jericho_money = 60 / 2

    # Calculate how much money Jericho owes in total
    total_debt = 14 + (jericho_money / 2)

    # Calculate how much money Jericho will have left after paying off his debts
    remaining_money = jericho_money - total_debt

    # Display how much money Jericho will have left
    result = remaining_money
    return result

print(solution())