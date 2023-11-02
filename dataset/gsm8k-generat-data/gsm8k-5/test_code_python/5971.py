def solution():
    # Price for buying 20 key chains in packs of 10
    price_10 = 2 * 20  # 2 packs of 10 for $20 each

    # Price for buying 20 key chains in packs of 4
    price_4 = 5 * 12  # 5 packs of 4 for $12 each

    # Difference in price
    savings = price_4 - price_10
    result = savings
    return result

print(solution())