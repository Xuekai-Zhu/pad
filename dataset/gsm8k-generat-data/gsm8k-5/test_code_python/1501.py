def solution():
    load_weight = 50000  # The tractor trailer has a load of 50000 pounds
    first_store_unload = 0.1  # 10% of the weight is unloaded at the first store
    second_store_unload = 0.2  # 20% of the remaining load is removed at the second store

    # Calculate the weight remaining after the first store
    remaining_weight_after_first_store = load_weight - (load_weight * first_store_unload)

    # Calculate the weight remaining after the second store
    remaining_weight_after_second_store = remaining_weight_after_first_store - (remaining_weight_after_first_store * second_store_unload)
    result = remaining_weight_after_second_store
    return result

print(solution())