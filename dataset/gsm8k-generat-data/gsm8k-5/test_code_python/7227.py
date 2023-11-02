def solution():
    money = 20  # Elizabeth has $20 to spend
    pen_price = 2  # Each pen costs $2
    pencil_price = 1.6  # Each pencil costs $1.60
    pens_wanted = 6  # Elizabeth wants to buy 6 pens

    # Calculate the total cost of the pens
    pen_cost = pens_wanted * pen_price

    # Calculate the remaining money after buying the pens
    remaining_money = money - pen_cost

    # Calculate the number of pencils Elizabeth can buy with the remaining money
    pencils_can_buy = remaining_money // pencil_price
    result = pencils_can_buy
    return result

print(solution())