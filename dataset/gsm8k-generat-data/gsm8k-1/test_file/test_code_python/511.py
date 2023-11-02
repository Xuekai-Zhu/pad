def solution():
    """Tara bought 8 packs of 5 canvas bags for $4 each. She painted them and sold them at a craft fair for $8 each. How much profit did she earn on her bags?"""
    packs_of_bags = 8
    bags_per_pack = 5
    cost_per_pack = 4
    bags_painted_and_sold = packs_of_bags * bags_per_pack
    revenue_per_bag = 8
    cost_per_bag = cost_per_pack / bags_per_pack
    profit_per_bag = revenue_per_bag - cost_per_bag
    total_profit = profit_per_bag * bags_painted_and_sold
    result = total_profit
    return result

print(solution())