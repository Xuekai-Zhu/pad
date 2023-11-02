def solution():
    """If you buy 2 packs of 500 mL milk, it will cost $2.50. If you buy them individually, they will cost $1.30 each. How much is your total savings from buying ten sets of 2 packs of 500 mL milk?"""
    pack_price = 2.50 / 2
    individual_price = 1.30
    savings_per_pack = individual_price - pack_price
    total_savings = savings_per_pack * 10 * 2
    result = total_savings
    return result

print(solution())