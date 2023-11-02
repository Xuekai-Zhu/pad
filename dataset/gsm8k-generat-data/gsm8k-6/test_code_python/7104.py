def solution():
    # Calculate the total weight of supplies already loaded on the truck
    total_weight_loaded = 100 * 100 + 10 * 60 + 50 * 50  # 100 boxes weighing 100 kgs each, 10 crates weighing 60 kgs each, 50 sacks weighing 50 kgs each
    remaining_weight = 13500 - total_weight_loaded  # maximum weight minus the weight already loaded

    # Calculate the number of bags weighing 40 kgs each that can still be loaded on the truck
    bags_weight = 40
    bags_loadable = remaining_weight // bags_weight
    result = bags_loadable
    return result

print(solution())