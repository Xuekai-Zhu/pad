def solution():
    suki_bags = 6.5  # Suki bought 6.5 bags of coffee beans
    suki_weight_per_bag = 22  # Each of Suki's bags weighed 22 kilograms
    jimmy_bags = 4.5  # Jimmy bought 4.5 bags of coffee beans
    jimmy_weight_per_bag = 18  # Each of Jimmy's bags weighed 18 kilograms
    repack_weight = 8  # The coffee beans were repackaged into 8-kilogram containers

    # Calculate the total weight of coffee beans Suki bought
    suki_total_weight = suki_bags * suki_weight_per_bag

    # Calculate the total weight of coffee beans Jimmy bought
    jimmy_total_weight = jimmy_bags * jimmy_weight_per_bag

    # Calculate the total weight of coffee beans
    total_weight = suki_total_weight + jimmy_total_weight

    # Calculate the number of containers needed
    containers_needed = total_weight // repack_weight

    result = containers_needed
    return result

print(solution())