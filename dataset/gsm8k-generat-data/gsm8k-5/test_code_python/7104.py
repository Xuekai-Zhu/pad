def solution():
    # Calculate the weight of the boxes and crates in the truck
    box_weight = 100 * 100  # Each box weighs 100 kgs
    crate_weight = 10 * 60  # Each crate weighs 60 kgs
    total_weight = box_weight + crate_weight

    # Calculate the weight of the sacks that can still be loaded in the truck
    remaining_weight = 13500 - total_weight  # Max weight minus weight of boxes and crates
    bags_weight = 50 * 40  # Each bag weighs 40 kgs
    bags_can_load = remaining_weight // bags_weight  # Integer division to get number of bags that can be loaded

    result = bags_can_load
    return result

print(solution())