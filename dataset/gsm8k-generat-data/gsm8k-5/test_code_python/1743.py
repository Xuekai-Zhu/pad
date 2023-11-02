def solution():
    shrimp_per_guest = 5  # Wayne plans on serving 5 shrimp per guest
    number_of_guests = 40  # Wayne will have 40 guests
    shrimp_per_pound = 20  # Each pound of shrimp contains 20 shrimp
    cost_per_pound = 17.00  # The cost of shrimp is $17.00 per pound

    # Calculate the total number of shrimp needed
    total_shrimp = shrimp_per_guest * number_of_guests

    # Calculate the total weight of shrimp needed in pounds
    total_weight = total_shrimp / shrimp_per_pound

    # Calculate the total cost of the shrimp
    total_cost = total_weight * cost_per_pound
    result = total_cost
    return result

print(solution())