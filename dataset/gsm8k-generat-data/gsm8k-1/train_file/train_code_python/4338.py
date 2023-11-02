def solution():
    """Matilda bought a smartphone for $300. Then she decided she wouldn't use it anyway and sold it for $255. What percentage of the initial cost did she lose?"""
    initial_cost = 300
    final_sale_price = 255
    percentage_lost = ((initial_cost - final_sale_price) / initial_cost) * 100
    result = percentage_lost
    return result

print(solution())