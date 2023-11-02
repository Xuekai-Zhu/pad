def solution():
    twice_money = 60  # Twice the money Jericho has is 60
    jericho_money = twice_money / 2  # Calculate Jericho's money
    annika_debt = 14  # Jericho owes Annika $14
    manny_debt = annika_debt / 2  # Jericho owes half as much to Manny

    # Calculate the total amount of debt Jericho owes
    total_debt = annika_debt + manny_debt

    # Calculate how much money Jericho will have left after paying off all his debts
    remaining_money = jericho_money - total_debt
    result = remaining_money
    return result

print(solution())