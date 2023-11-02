def solution():
    package_weight = 2  # Each package of sausages weighs 2 pounds
    num_packages = 3  # Jake buys 3 packages of sausages
    price_per_pound = 4  # The price per pound of sausages is $4

    # Calculate the total weight of sausages Jake buys
    total_weight = package_weight * num_packages

    # Calculate the total cost of sausages Jake buys
    total_cost = total_weight * price_per_pound
    result = total_cost
    return result

print(solution())