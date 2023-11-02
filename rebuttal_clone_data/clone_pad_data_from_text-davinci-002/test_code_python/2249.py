def solution():
    packs_sold_high = 6
    packs_sold_low = 4
    price_per_pack = 60
    hours_sold = 15
    total_packs_sold_high = packs_sold_high * hours_sold
    total_packs_sold_low = packs_sold_low * hours_sold
    total_revenue_high = total_packs_sold_high * price_per_pack
    total_revenue_low = total_packs_sold_low * price_per_pack
    difference = total_revenue_high - total_revenue_low
    result = difference
    return result

print(solution())