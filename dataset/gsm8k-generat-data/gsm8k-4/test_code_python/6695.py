def solution():
    """Lighters cost $1.75 each at the gas station, or $5.00 per pack of twelve on Amazon. How much would Amanda save by buying 24 lighters online instead of at the gas station?"""
    # Define the price of a lighter and the price of a pack of twelve
    gas_station_price = 1.75
    amazon_price = 5.00 / 12

    # Calculate the total cost of buying 24 lighters at the gas station
    gas_station_cost = 24 * gas_station_price

    # Calculate the total cost of buying 24 lighters on Amazon
    amazon_cost = 24 * amazon_price

    # Calculate the savings of buying on Amazon
    savings = gas_station_cost - amazon_cost

    # Return the result
    result = savings
    return result

print(solution())