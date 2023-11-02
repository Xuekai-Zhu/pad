def solution():
    blocks_to_bus_stop = 5
    blocks_on_bus = 7

    # Calculate the total number of blocks traveled to the coffee shop
    total_blocks_to_coffee_shop = blocks_to_bus_stop + blocks_on_bus

    # Calculate the total number of blocks traveled round trip
    total_blocks_round_trip = total_blocks_to_coffee_shop * 2

    result = total_blocks_round_trip
    return result

print(solution())