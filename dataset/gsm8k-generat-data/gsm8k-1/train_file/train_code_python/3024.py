def solution():
    """A store transports fresh vegetables in crates and cartons using its delivery truck. One crate of vegetables weighs 4 kilograms and one carton 3 kilograms. How much will a load of 12 crates, and 16 cartons of vegetables weigh?"""
    crate_weight = 4
    carton_weight = 3
    crates = 12
    cartons = 16
    total_weight = (crate_weight * crates) + (carton_weight * cartons)
    result = total_weight
    return result

print(solution())