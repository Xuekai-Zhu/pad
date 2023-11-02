def solution():
    unit_weight = 4  # pounds
    total_weight = 100  # pounds
    num_packages_1 = 10
    num_packages_2 = 7

    # Calculate the total number of packages of ground beef delivered by the first two butchers
    num_packages_delivered = num_packages_1 + num_packages_2

    # Calculate the total weight of ground beef delivered by the first two butchers
    weight_delivered = num_packages_delivered * unit_weight

    # Calculate the number of packages delivered by the third butcher
    num_packages_3 = (total_weight - weight_delivered) / unit_weight
    result = num_packages_3
    return result

print(solution())