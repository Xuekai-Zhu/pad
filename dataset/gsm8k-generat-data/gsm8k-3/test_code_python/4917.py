def solution():
    """Lizzy has to ship 540 pounds of fish that are packed into 30-pound crates. If the shipping cost of each crate is $1.5, how much will Lizzy pay for the shipment?"""
    # Calculate the number of crates needed
    num_crates = 540 / 30

    # Calculate the total cost of shipping
    total_cost = num_crates * 1.5

    # Display the total cost
    result = total_cost
    return result

print(solution())