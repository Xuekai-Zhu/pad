def solution():
    # Calculate the total amount of money Pete has in his wallet
    wallet_money = (2 * 20) + (4 * 10)  # Pete has two $20 bills and four $10 bills

    # Calculate the remaining amount of money Pete needs to pay off his bike
    remaining_money = 90 - wallet_money

    # Calculate the number of bottles Pete needs to return to the store to get the remaining money
    bottles_needed = remaining_money / 0.5  # The store pays 50 cents per bottle

    result = bottles_needed
    return result

print(solution())