def solution():
    """Lighters cost $1.75 each at the gas station, or $5.00 per pack of twelve on Amazon. How much would Amanda save by buying 24 lighters online instead of at the gas station?"""
    gas_station_price = 1.75
    amazon_price_per_lighter = 5 / 12
    amazon_price_for_24 = 24 * amazon_price_per_lighter
    gas_station_price_for_24 = 24 * gas_station_price
    savings = gas_station_price_for_24 - amazon_price_for_24
    result = savings
    return result

print(solution())