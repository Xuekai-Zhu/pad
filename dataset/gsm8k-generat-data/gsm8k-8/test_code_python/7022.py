def solution():
    # Calculate the total weight of Suki's coffee beans
    suki_total_weight = 6.5 * 22

    # Calculate the total weight of Jimmy's coffee beans
    jimmy_total_weight = 4.5 * 18

    # Calculate the combined weight of Suki and Jimmy's coffee beans
    total_weight = suki_total_weight + jimmy_total_weight

    # Calculate the number of 8-kilogram containers they need
    num_containers = total_weight / 8

    result = int(num_containers)
    return result

print(solution())