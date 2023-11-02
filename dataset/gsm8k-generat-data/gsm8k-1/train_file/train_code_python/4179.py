def solution():
    """Maria buys a large bar of French soap that lasts her for 2 months. She spends $8.00 per bar of soap. If she wants to stock up for the entire year, how much will she spend on soap?"""
    soap_cost = 8
    bars_per_year = 12 // 2 # 1 bar lasts for 2 months, so 12 months / 2 = 6 bars per year
    total_cost = soap_cost * bars_per_year
    result = total_cost
    return result

print(solution())