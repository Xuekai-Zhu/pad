def solution():
    gas_station_price = 1.75
    amazon_price_per_lighter = 5.00/12
    num_lighters = 24

    # Calculate the total cost of buying 24 lighters at the gas station
    gas_station_cost = num_lighters * gas_station_price

    # Calculate the total cost of buying 24 lighters on Amazon
    amazon_cost = num_lighters * amazon_price_per_lighter

    # Calculate the amount saved by buying on Amazon instead of the gas station
    amount_saved = gas_station_cost - amazon_cost
    result = amount_saved
    return result

print(solution())