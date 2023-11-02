def solution():
    price_at_gas_station = 1.75  # Price per lighter at gas station
    price_per_pack_on_amazon = 5.00  # Price per pack of 12 on Amazon
    lighter_per_pack = 12  # Number of lighters in a pack

    # Calculate the cost of buying 24 lighters at the gas station
    cost_at_gas_station = 24 * price_at_gas_station

    # Calculate the number of packs needed to buy 24 lighters on Amazon
    packs_on_amazon = 2  # 24 lighters / 12 lighters per pack = 2 packs

    # Calculate the cost of buying 2 packs on Amazon
    cost_on_amazon = packs_on_amazon * price_per_pack_on_amazon

    # Calculate the amount Amanda would save by buying 24 lighters on Amazon
    savings = cost_at_gas_station - cost_on_amazon
    result = savings
    return result

print(solution())