def solution():
    """Leah earned $28 working odd jobs around the neighborhood. She spent a seventh of it on a milkshake and put half of the rest in her savings account. She left the remaining money in her wallet. Her dog got ahold of her wallet and shredded all the money inside but $1. How many dollars did Leah lose?"""
    # Define the amount Leah earned
    total_earned = 28

    # Calculate the amount Leah spent on a milkshake
    milkshake_cost = total_earned / 7

    # Calculate the amount Leah had left after buying the milkshake
    remaining_amount = total_earned - milkshake_cost

    # Calculate the amount Leah put into her savings account
    savings_amount = remaining_amount / 2

    # Calculate the amount Leah had in her wallet
    wallet_amount = remaining_amount - savings_amount

    # Calculate the amount of money Leah lost after her dog shredded her wallet
    lost_amount = wallet_amount - 1

    # return the result
    result = lost_amount
    return result

print(solution())