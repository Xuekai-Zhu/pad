def solution():
    bags_suki = 6.5
    bags_jimmy = 4.5
    weight_suki = 22
    weight_jimmy = 18
    total_bags = bags_suki + bags_jimmy
    total_weight = weight_suki * bags_suki + weight_jimmy * bags_jimmy
    weight_per_container = 8
    containers = total_weight / weight_per_container
    result = containers
    return result

print(solution())