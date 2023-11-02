def solution():
    """Linda makes and sells necklaces at craft fairs. At her most recent fair she sold 4 necklaces and 8 rings for a total of $80. If each necklace costs $12, how much does each ring cost?"""
    necklaces_sold = 4
    rings_sold = 8
    total_sales = 80
    necklace_price = 12
    ring_price = (total_sales - (necklaces_sold * necklace_price)) / rings_sold
    result = ring_price
    return result

print(solution())