def solution():
    """Asia bought a homecoming dress on sale for $140. It was originally priced at $350. What percentage off did she get at the sale?"""
    original_price = 350
    sale_price = 140
    discount = (original_price - sale_price) / original_price
    percent_off = discount * 100
    result = percent_off
    return result

print(solution())