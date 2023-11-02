def solution():
    """Lighters cost $1.75 each at the gas station, or $5.00 per pack of twelve on Amazon. How much would Amanda save by buying 24 lighters online instead of at the gas station?"""
    gas_station_price = 1.75
    amazon_price_per_lighter = 5 / 12
    num_lighters = 24
    gas_station_total = num_lighters * gas_station_price
    amazon_total = num_lighters * amazon_price_per_lighter
    savings = gas_station_total - amazon_total
    result = savings
    return result

print(solution())