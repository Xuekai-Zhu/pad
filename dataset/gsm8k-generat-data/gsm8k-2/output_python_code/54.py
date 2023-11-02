def solution():
    """Leah earned $28 working odd jobs around the neighborhood. She spent a seventh of it on a milkshake and put half of the rest in her savings account. She left the remaining money in her wallet. Her dog got ahold of her wallet and shredded all the money inside but $1. How many dollars did Leah lose?"""
    total_earnings = 28
    milkshake_cost = total_earnings / 7
    remaining_money = total_earnings - milkshake_cost
    savings_account = remaining_money / 2
    remaining_in_wallet = remaining_money - savings_account - 1
    lost_money = remaining_in_wallet
    result = lost_money
    return result

print(solution())