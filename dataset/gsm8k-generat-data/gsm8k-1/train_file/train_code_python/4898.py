def solution():
    """Robin wants to buy jelly bracelets for her friends. She decides to buy one bracelet for each letter of the first name of her friends. Her friends are Jessica, Tori, Lily and Patrice. If each jelly bracelet costs $2, what is the total she will spend in dollars?"""
    friend_names = ['Jessica', 'Tori', 'Lily', 'Patrice']
    total_bracelets = 0
    for name in friend_names:
        name_length = len(name)
        total_bracelets += name_length
    cost_per_bracelet = 2
    total_cost = total_bracelets * cost_per_bracelet
    result = total_cost
    return result

print(solution())