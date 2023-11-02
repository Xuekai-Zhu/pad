def solution():
    bridge_limit = 20000  # The bridge can hold 20,000 pounds
    truck_weight = 12000  # Donna's empty truck weighs 12,000 pounds
    crate_weight = 50  # Each crate of soda weighs 50 pounds
    num_crates = 20  # Donna is carrying 20 crates of soda
    dryer_weight = 3000  # Each dryer weighs 3,000 pounds
    num_dryers = 3  # Donna is carrying 3 dryers
    soda_weight = crate_weight * num_crates  # Total weight of the soda
    produce_weight = 2 * soda_weight  # Twice the weight of the soda is fresh produce

    # Calculate the total weight of Donna's fully loaded truck
    total_weight = truck_weight + soda_weight + (num_dryers * dryer_weight) + produce_weight

    result = total_weight
    return result

print(solution())