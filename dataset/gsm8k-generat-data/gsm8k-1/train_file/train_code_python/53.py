def solution():
    """Leah earned $28 working odd jobs around the neighborhood. She spent a seventh of it on a milkshake and put half of the rest in her savings account. She left the remaining money in her wallet. Her dog got ahold of her wallet and shredded all the money inside but $1. How many dollars did Leah lose?"""
    initial_earnings = 28
    spent_on_milkshake = initial_earnings / 7
    remaining = initial_earnings - spent_on_milkshake
    saved = remaining / 2
    lost = remaining - saved - 1
    result = lost
    return result

print(solution())