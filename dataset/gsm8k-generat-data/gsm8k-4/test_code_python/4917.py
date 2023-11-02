def solution():
    """Lizzy has to ship 540 pounds of fish that are packed into 30-pound crates. If the shipping cost of each crate is $1.5, how much will Lizzy pay for the shipment?"""
    # Define the weight of each crate and the number of crates needed
    crate_weight = 30
    num_crates = 540 / crate_weight

    # Calculate the total cost of shipping
    shipping_cost = num_crates * 1.5

    # return the result
    result = shipping_cost
    return result

print(solution())