def solution():
    """Moore's family compared mobile phone plans to get the best deal. At T-Mobile, the family plan costs $50 per month for the first two lines and $16 for each additional line. At M-Mobile, the family plan costs $45 for the first two lines and $14 for each additional line. Moore's family needs to purchase 5 cell phone lines. How much cheaper is the M-Mobile than T-Mobile?"""
    tmobile_total_cost = 2 * 50 + 3 * 16
    mmobile_total_cost = 2 * 45 + 3 * 14
    cheaper_amount = tmobile_total_cost - mmobile_total_cost
    result = cheaper_amount
    return result

print(solution())