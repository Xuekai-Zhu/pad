def solution():
    crate_weight = 4  # One crate of vegetables weighs 4 kilograms
    carton_weight = 3  # One carton of vegetables weighs 3 kilograms
    num_crates = 12  # The delivery truck has 12 crates of vegetables
    num_cartons = 16  # The delivery truck has 16 cartons of vegetables

    # Calculate the total weight of the crates and cartons
    total_weight = (crate_weight * num_crates) + (carton_weight * num_cartons)
    result = total_weight
    return result

print(solution())