def solution():
    """Leah earned $28 working odd jobs around the neighborhood. She spent a seventh of it on a milkshake and put half of the rest in her savings account. She left the remaining money in her wallet. Her dog got ahold of her wallet and shredded all the money inside but $1. How many dollars did Leah lose?"""
    
    money_earned = 28
    money_spent = money_earned / 7
    money_saved = (money_earned - money_spent) / 2
    money_left = money_earned - money_spent - money_saved
    money_lost = money_left - 1
    result = money_lost
    
    return result

print(solution())