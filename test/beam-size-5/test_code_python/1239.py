def solution():
    num_sticks = 30  # Archie buys 30 sticks to a bag
    cost_per_stick = 18.00  # The cost per stick of jerky is $18.00
    discount = 3.00  # Archie gets $3.00 off a bag

    # Calculate the total cost of the jerky before discount
    total_cost_before_discount = num_sticks * cost_per_stick

    # Calculate the cost per bag after discount
    cost_per_bag_after_discount = total_cost_before_discount - discount

    # Calculate the cost per stick in cents
    cost_per_stick_cents = cost_per_bag_after_discount * 100
    result = cost_per_stick_cents
    return result

print(solution())