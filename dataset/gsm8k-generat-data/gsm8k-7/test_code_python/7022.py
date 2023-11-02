def solution():
    suki_bags = 6.5
    suki_weight = 22
    jimmy_bags = 4.5
    jimmy_weight = 18
    container_weight = 8

    # Calculate the total weight of Suki's coffee beans
    suki_total_weight = suki_bags * suki_weight

    # Calculate the total weight of Jimmy's coffee beans
    jimmy_total_weight = jimmy_bags * jimmy_weight

    # Calculate the total weight of all coffee beans
    total_weight = suki_total_weight + jimmy_total_weight

    # Calculate the number of containers needed
    num_containers = total_weight / container_weight

    result = num_containers
    return result

print(solution())