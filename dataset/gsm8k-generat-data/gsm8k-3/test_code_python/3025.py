def solution():
    """A store transports fresh vegetables in crates and cartons using its delivery truck. One crate of vegetables weighs 4 kilograms and one carton 3 kilograms. How much will a load of 12 crates, and 16 cartons of vegetables weigh?"""
    # Define the weight of one crate and one carton
    CRATE_WEIGHT = 4
    CARTON_WEIGHT = 3

    # Define the number of crates and cartons
    crate_count = 12
    carton_count = 16

    # Calculate the total weight of the load
    total_weight = crate_count * CRATE_WEIGHT + carton_count * CARTON_WEIGHT

    # Display the total weight of the load
    result = total_weight
    return result

print(solution())