def solution():
    """Jenny goes to the florist to buy some flowers. Roses cost $2 each and $15 for a dozen. If she bought 15 roses and arrived with five 5 dollar bills and they only have quarters for change, how many quarters does she leave with?"""
    roses = 15
    price_per_rose = 2
    price_per_dozen = 15
    dozen = roses // 12
    remainder = roses % 12
    total_price = dozen * price_per_dozen + remainder * price_per_rose
    change = 5 * 5 - total_price
    num_quarters = change // 0.25
    result = num_quarters
    return result

print(solution())