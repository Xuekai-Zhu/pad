def solution():
    
    package_weight = 4
    total_weight = 100
    first_delivery = 10 * package_weight
    second_delivery = 7 * package_weight
    third_delivery = total_weight - first_delivery - second_delivery
    packages_delivered = third_delivery / package_weight
    result = packages_delivered
    return result

print(solution())