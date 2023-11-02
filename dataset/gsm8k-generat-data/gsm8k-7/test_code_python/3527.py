def solution():
    first_package_dist = 10
    second_package_dist = 28
    third_package_dist = second_package_dist / 2
    total_distance = first_package_dist + second_package_dist + third_package_dist
    total_pay = 104
    pay_per_mile = total_pay / total_distance
    result = pay_per_mile
    return result

print(solution())