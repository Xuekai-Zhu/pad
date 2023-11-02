def solution():
    """A gift shop sells bracelets at $15 each, a gold heart necklace at $10, and a personalized coffee mug at $20. Raine buys three bracelets, two gold heart necklaces, and one coffee mug for her friends. How much change does Raine get back if she gives a one hundred dollar bill?"""
    bracelets = 3
    necklace = 2
    mug = 1
    cost = (bracelets * 15) + (necklace * 10) + (mug * 20)
    change = 100 - cost
    result = change
    return result

print(solution())