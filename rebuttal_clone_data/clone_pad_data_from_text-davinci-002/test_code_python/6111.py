def solution():
    gas_price_1 = 3
    gas_price_2 = 3.5
    gas_price_3 = 4
    gas_price_4 = 4.5
    tank_size = 12
    gas_used_1 = tank_size
    gas_used_2 = tank_size
    gas_used_3 = tank_size
    gas_used_4 = tank_size
    total_gas_price = gas_price_1 * gas_used_1 + gas_price_2 * gas_used_2 + gas_price_3 * gas_used_3 + gas_price_4 * gas_used_4
    result = total_gas_price
    return result

print(solution())