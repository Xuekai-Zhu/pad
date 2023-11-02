def solution():
    # Find the value of 3 dimes and 7 nickels
    value_of_dimes = 0.3  # 3 dimes = 30 cents
    value_of_nickels = 0.35  # 7 nickels = 35 cents

    # Find the amount of money needed to trade for 20 quarters using dimes
    quarters_from_dimes = 20
    dimes_needed = quarters_from_dimes * 3
    money_for_quarters_from_dimes = dimes_needed * 0.1

    # Find the amount of money needed to trade for 20 quarters using nickels
    quarters_from_nickels = 20
    nickels_needed = quarters_from_nickels * 7
    money_for_quarters_from_nickels = nickels_needed * 0.05

    # Find how much money Mac lost
    amount_lost = (money_for_quarters_from_dimes + money_for_quarters_from_nickels) - 10  # 10 dollars for 40 quarters
    result = amount_lost
    return result

print(solution())