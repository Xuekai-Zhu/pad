def solution():
    mom_money = 100  # Their mom gave them $100 to spend
    mildred_money_spent = 25  # Mildred spent $25 at the market
    candice_money_spent = 35  # Candice spent $35 at the market

    # Calculate the total money spent by both of them
    total_money_spent = mildred_money_spent + candice_money_spent

    # Calculate the amount of money left after spending
    money_left = mom_money - total_money_spent
    result = money_left
    return result

print(solution())