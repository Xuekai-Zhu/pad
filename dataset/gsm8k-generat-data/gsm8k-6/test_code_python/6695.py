def solution():
    # Calculate the cost of buying 24 lighters at the gas station and on Amazon
    gas_station_cost = 24 * 1.75
    amazon_pack_cost = 5 * (24 // 12)  # round down to the nearest multiple of 12
    amazon_individual_cost = (24 % 12) * 1.75  # calculate the remaining individual lighters
    amazon_cost = amazon_pack_cost + amazon_individual_cost

    # Calculate the amount Amanda would save by buying 24 lighters online instead of at the gas station
    amount_saved = gas_station_cost - amazon_cost
    result = amount_saved
    return result

print(solution())