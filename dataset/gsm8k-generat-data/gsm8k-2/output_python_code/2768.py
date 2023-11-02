def solution():
    """Linda makes and sells necklaces at craft fairs. At her most recent fair she sold 4 necklaces and 8 rings for a total of $80. If each necklace costs $12, how much does each ring cost?"""
    total_sales = 80
    necklace_price = 12
    necklace_count = 4
    necklace_sales = necklace_count * necklace_price
    ring_sales = total_sales - necklace_sales
    ring_count = 8
    ring_price = ring_sales / ring_count
    result = ring_price
    return result

print(solution())