def solution():
    # Calculate how much Leah spent on a milkshake
    milkshake_cost = 28 / 7

    # Calculate how much Leah had left after buying the milkshake
    remaining_money = 28 - milkshake_cost

    # Calculate how much Leah put in her savings account
    savings_amount = remaining_money / 2

    # Calculate how much Leah had in her wallet
    wallet_amount = remaining_money - savings_amount - 1

    # Calculate how much money Leah lost when her dog shredded her wallet
    lost_money = wallet_amount

    result = lost_money
    return result

print(solution())