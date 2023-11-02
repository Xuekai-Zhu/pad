def solution():
    """A banana tree has 100 bananas left after Raj cut some bananas from it. If Raj has eaten 70 bananas and has twice as many remaining in his basket, how many bananas were on the tree initially?"""
    # Let x be the initial number of bananas on the tree
    # After Raj cuts some bananas, there are x-y bananas left on the tree
    # Raj eats 70 bananas, so he has x-y-70 bananas left in his basket
    # Raj has twice as many bananas in his basket as are left on the tree, so:
    # x-y-70 = 2(x-y)
    # Simplifying this equation gives:
    # x = 230
    initial_bananas = 230
    result = initial_bananas
    return result

print(solution())