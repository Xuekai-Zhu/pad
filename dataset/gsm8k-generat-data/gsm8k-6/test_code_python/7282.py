def solution():
    # Convert 200 quarters to dollars
    quarters_to_dollars = 200 * 0.25

    # Calculate the total amount of money Oliver has before giving money to his sister
    total_money = 40 + quarters_to_dollars

    # Calculate the amount of money Oliver gives to his sister
    money_to_sister = 5 + (120 * 0.25)

    # Calculate the total amount of money Oliver has after giving money to his sister
    remaining_money = total_money - money_to_sister
    result = remaining_money
    return result

print(solution())