def solution():
    # Calculate the total weight of coffee beans that Suki bought
    suki_weight = 6.5 * 22

    # Calculate the total weight of coffee beans that Jimmy bought
    jimmy_weight = 4.5 * 18

    # Calculate the total weight of coffee beans
    total_weight = suki_weight + jimmy_weight

    # Calculate the number of containers used
    num_containers = total_weight / 8

    result = num_containers
    return result

print(solution())