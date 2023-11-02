def solution():
    """Leah earned $28 working odd jobs around the neighborhood. She spent a seventh of it on a milkshake and put half of the rest in her savings account. She left the remaining money in her wallet. Her dog got ahold of her wallet and shredded all the money inside but $1. How many dollars did Leah lose?"""
    # Define the initial amount of money Leah earned
    initial_money = 28

    # Calculate the amount of money Leah spent on a milkshake
    milkshake_cost = initial_money / 7

    # Calculate the amount of money Leah had left after buying the milkshake
    remaining_money = initial_money - milkshake_cost

    # Calculate the amount of money Leah put in her savings account
    savings = remaining_money / 2

    # Calculate the amount of money Leah had left in her wallet
    wallet_money = remaining_money - savings

    # Subtract $1, as that was not shredded by her dog
    shredded_money = initial_money - milkshake_cost - savings - 1

    # Return the amount of money Leah lost
    result = shredded_money
    return result

print(solution())