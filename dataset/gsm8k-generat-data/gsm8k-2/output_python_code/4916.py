def solution():
    """Lizzy has to ship 540 pounds of fish that are packed into 30-pound crates. If the shipping cost of each crate is $1.5, how much will Lizzy pay for the shipment?"""
    fish_weight = 540
    crate_weight = 30
    num_crates = fish_weight // crate_weight + (1 if fish_weight % crate_weight != 0 else 0)
    shipping_cost = 1.5
    total_cost = num_crates * shipping_cost
    result = total_cost
    return result

print(solution())