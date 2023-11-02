def solution():
    """Hakeem has always loved artichoke dip and plans to make it this weekend. He has $15 dollars to buy artichokes and can find the rest of the ingredients at home. It takes 3 artichokes to make 5 ounces of dip. How many ounces can he make if artichokes cost $1.25 each?"""
    budget = 15
    artichoke_price = 1.25
    max_artichokes = budget // artichoke_price
    ounces_per_artichoke = 5/3
    max_ounces = max_artichokes * ounces_per_artichoke
    result = max_ounces
    return result

print(solution())