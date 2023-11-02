def solution():
    """A gift shop sells bracelets at $15 each, a gold heart necklace at $10, and a personalized coffee mug at $20. Raine buys three bracelets, two gold heart necklaces, and one coffee mug for her friends. How much change does Raine get back if she gives a one hundred dollar bill?"""
    bracelet_price = 15
    necklace_price = 10
    mug_price = 20
    num_bracelets = 3
    num_necklaces = 2
    num_mugs = 1
    total_price = (bracelet_price * num_bracelets) + (necklace_price * num_necklaces) + (mug_price * num_mugs)
    change = 100 - total_price
    result = change
    return result

print(solution())