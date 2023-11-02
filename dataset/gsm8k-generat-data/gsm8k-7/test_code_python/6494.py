def solution():
    bridge_limit = 20000
    truck_weight = 12000

    soda_crates = 20
    soda_weight = 50
    total_soda_weight = soda_crates * soda_weight

    dryers = 3
    dryer_weight = 3000
    total_dryer_weight = dryers * dryer_weight

    produce_weight = total_soda_weight * 2

    # Calculate the total weight of the truck and its cargo
    total_weight = truck_weight + total_soda_weight + total_dryer_weight + produce_weight

    result = total_weight
    return result

print(solution())