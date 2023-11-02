def solution():
    # Calculate the total amount of water added to the pool
    total_water_added = 8 + (2 * 10) + 14

    # Calculate the total amount of water lost due to the leak
    total_water_lost = 8

    # Calculate the net change in water level in the pool
    net_water_change = total_water_added - total_water_lost

    # Calculate the final amount of water in the pool
    final_amount_of_water = net_water_change * 5

    result = final_amount_of_water
    return result

print(solution())