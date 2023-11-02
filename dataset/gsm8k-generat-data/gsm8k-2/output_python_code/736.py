def solution():
    """Michael has 4 packs of crayons and wants to buy 2 more. One pack of crayons costs $2.5. How much are all the packs of crayons Michael will have after the purchase worth?"""
    packs_before_purchase = 4
    packs_to_buy = 2
    pack_price = 2.5
    total_packs = packs_before_purchase + packs_to_buy
    total_price = total_packs * pack_price
    result = total_price
    return result

print(solution())