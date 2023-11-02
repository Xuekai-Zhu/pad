def solution():
    """If you buy 2 packs of 500 mL milk, it will cost $2.50. If you buy them individually, they will cost $1.30 each. How much is your total savings from buying ten sets of 2 packs of 500 mL milk?"""
    packs_per_set = 2
    volume_per_pack = 500
    price_per_set = 2.50
    price_per_individual_pack = 1.30
    sets_to_buy = 10
    total_price_with_sets = price_per_set * sets_to_buy
    total_price_without_sets = (packs_per_set * volume_per_pack * price_per_individual_pack) * sets_to_buy
    savings = total_price_without_sets - total_price_with_sets
    result = savings
    return result

print(solution())