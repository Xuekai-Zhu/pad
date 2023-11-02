def solution():
    # Calculate the total bill for dinner
    total_money = 40 * 2  # Aaron and Carson each saved $40
    dinner_bill = (3/4) * total_money

    # Calculate the total cost of ice cream
    remaining_money = total_money - dinner_bill - 2  # 2 dollars left as change
    ice_cream_cost = (remaining_money - 2) / 2  # each brother gets $1 change back, so $2 is subtracted from remaining money
    scoops_each = ice_cream_cost / 1.5  # cost of each scoop is $1.5
    result = int(scoops_each)
    return result

print(solution())