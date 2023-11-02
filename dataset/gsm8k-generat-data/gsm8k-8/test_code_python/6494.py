def solution():
    # Define the weight of Donna's empty truck
    empty_truck_weight = 12000

    # Define the weight of the soda crates
    soda_crate_weight = 50
    num_soda_crates = 20
    soda_total_weight = soda_crate_weight * num_soda_crates

    # Define the weight of the dryers
    dryer_weight = 3000
    num_dryers = 3
    dryer_total_weight = dryer_weight * num_dryers

    # Define the weight of the fresh produce
    fresh_produce_weight = soda_total_weight * 2

    # Calculate the total weight of the truck
    total_weight = empty_truck_weight + soda_total_weight + dryer_total_weight + fresh_produce_weight

    result = total_weight
    return result

print(solution())