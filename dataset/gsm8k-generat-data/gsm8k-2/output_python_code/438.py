def solution():
    """Timothy has $50 to spend at a souvenir shop. He sees some t-shirts that cost $8 each, key chains that sell 3 pieces for $2, and bags that cost $10 each. Timothy buys 2 t-shirts and 2 bags. How many pieces of key chains can he buy with the amount of money he has left?"""
    budget = 50
    tshirt_price = 8
    bag_price = 10
    keychain_price = 2/3
    total_spent = (2*tshirt_price) + (2*bag_price)
    budget_left = budget - total_spent
    keychains_bought = budget_left // keychain_price
    result = keychains_bought
    return result

print(solution())