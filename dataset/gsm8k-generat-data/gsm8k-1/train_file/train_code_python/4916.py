def solution():
    """Lizzy has to ship 540 pounds of fish that are packed into 30-pound crates. If the shipping cost of each crate is $1.5, how much will Lizzy pay for the shipment?"""
    total_weight = 540
    crate_weight = 30
    num_crates = total_weight / crate_weight
    cost_per_crate = 1.5
    total_cost = num_crates * cost_per_crate
    result = total_cost
    return result

print(solution())