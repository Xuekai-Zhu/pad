def solution():
    strawberries_needed = 4
    raspberries_needed = 4
    heavy_cream_needed = 2
    strawberry_package_cost = 3.00
    raspberry_package_cost = 5.00
    heavy_cream_cost = 4.00
    strawberry_cost = strawberries_needed / 2 * strawberry_package_cost
    raspberry_cost = raspberries_needed / 2 * raspberry_package_cost
    heavy_cream_cost = heavy_cream_needed / 4 * heavy_cream_cost
    total_cost = strawberry_cost + raspberry_cost + heavy_cream_cost
    result = total_cost
    return result

print(solution())