def solution():
    """Robin wants to buy jelly bracelets for her friends. She decides to buy one bracelet for each letter of the first name of her friends. Her friends are Jessica, Tori, Lily, and Patrice. If each jelly bracelet costs $2, what is the total she will spend in dollars?"""
    names = ['Jessica', 'Tori', 'Lily', 'Patrice']
    total_bracelets = sum([len(name) for name in names])
    total_cost = total_bracelets * 2
    result = total_cost
    return result

print(solution())