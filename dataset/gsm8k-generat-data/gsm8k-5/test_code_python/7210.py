def solution():
    calories_per_chip = 10  # Each chip has 10 calories
    chips_per_bag = 24  # Each bag has 24 chips
    cost_per_bag = 2  # Each bag costs $2

    # Calculate the number of bags Peter needs to eat to consume 480 calories
    total_chips_needed = 480 / calories_per_chip
    bags_needed = total_chips_needed / chips_per_bag

    # Calculate the total cost of the chips Peter needs to eat
    total_cost = bags_needed * cost_per_bag
    result = total_cost
    return result

print(solution())