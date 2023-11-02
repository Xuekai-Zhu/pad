def solution():
    # Calculate the cost of 24 lighters at the gas station
    gas_station_cost = 24 * 1.75

    # Calculate the cost of 24 lighters on Amazon
    amazon_cost = (24 // 12) * 5
    if 24 % 12 != 0:
        amazon_cost += (24 % 12) * 1.75

    # Calculate the amount saved
    amount_saved = gas_station_cost - amazon_cost
    result = amount_saved
    return result

print(solution())