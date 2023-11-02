def solution():
    """A kiddy gift shop sells bracelets at $4 each, keychains at $5 each, and coloring books at $3 each. Paula and Olive want to buy presents for their friends. Paula buys two bracelets and a keychain, while Olive buys a coloring book and a bracelet. How much do Paula and Olive spend in total?"""
    paula_total = 2 * 4 + 5
    olive_total = 3 + 4
    total_spent = paula_total + olive_total
    result = total_spent
    return result

print(solution())