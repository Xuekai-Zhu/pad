def solution():
    # Calculate the amount spent on the milkshake
    milkshake_cost = 28 / 7  # a seventh of $28

    # Calculate the amount of money left after buying the milkshake
    remaining_money = 28 - milkshake_cost  # $28 - cost of milkshake

    # Calculate the amount placed in savings account
    savings_amount = remaining_money / 2

    # Calculate the amount of money left in the wallet before the dog shredded it
    wallet_amount = remaining_money - savings_amount

    # Calculate the amount of money Leah lost when her dog shredded her wallet
    lost_money = wallet_amount - 1  # $1 left in wallet after shredding by dog

    result = lost_money
    return result

print(solution())