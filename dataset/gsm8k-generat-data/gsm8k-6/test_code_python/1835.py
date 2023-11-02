def solution():
    # Calculate the total amount of money saved by the three kids
    pennies_total = 200 / 100  # convert pennies to dollars
    nickels_total = 100 * 0.05  # convert nickels to dollars
    dimes_total = 330 * 0.1  # convert dimes to dollars
    total_money_saved = pennies_total + nickels_total + dimes_total
    result = total_money_saved
    return result

print(solution())