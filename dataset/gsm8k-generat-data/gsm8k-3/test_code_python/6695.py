def solution():
    """Lighters cost $1.75 each at the gas station, or $5.00 per pack of twelve on Amazon. How much would Amanda save by buying 24 lighters online instead of at the gas station?"""
    # Define the cost of one lighter at the gas station
    GAS_STATION_PRICE = 1.75

    # Define the cost of one pack of twelve lighters on Amazon
    AMAZON_PRICE = 5.00

    # Calculate the cost of 24 lighters at the gas station
    gas_station_cost = 24 * GAS_STATION_PRICE

    # Calculate the cost of 24 lighters on Amazon
    packs_needed = 2
    single_lighters_needed = 0
    amazon_cost = packs_needed * AMAZON_PRICE

    # Calculate the amount saved by buying on Amazon instead of at the gas station
    savings = gas_station_cost - amazon_cost

    # Display the amount saved
    result = savings
    return result

print(solution())