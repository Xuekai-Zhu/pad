def solution():
    total_earnings = 28  # Leah earned $28
    milkshake_cost = total_earnings / 7  # Leah spent a seventh of her earnings on a milkshake
    remaining_money = total_earnings - milkshake_cost  # Leah has remaining earnings after buying the milkshake
    savings_account = remaining_money / 2  # Leah put half of the remaining money in her savings account
    remaining_wallet_money = remaining_money - savings_account - 1  # Leah left the remaining money in her wallet, but her dog shredded it except $1

    # Calculate the amount of money Leah lost
    lost_money = total_earnings - remaining_wallet_money - 1
    result = lost_money
    return result

print(solution())