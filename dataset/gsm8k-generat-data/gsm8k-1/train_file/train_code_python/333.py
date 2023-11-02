def solution():
    """Martha needs 4 cups of berries and 2 cups of heavy cream to make 1 quart of ice cream. She wants to make 1 quart of strawberry ice cream and 1 quart of raspberry ice cream. At the farmers market, the 2 cup packages of strawberries are $3.00 each and the 2 cup package of raspberries are $5.00 each. The heavy cream is sold for $4.00 for a 4 cup container. How much will it cost her to make 1 quart of each ice cream?"""
    berries_per_quart = 4
    cream_per_quart = 2
    strawberries_cost_per_package = 3
    raspberries_cost_per_package = 5
    cream_cost_per_container = 4
    strawberries_packages_needed = berries_per_quart / 2
    raspberries_packages_needed = berries_per_quart / 2
    cream_containers_needed = cream_per_quart / 4
    total_strawberry_cost = strawberries_packages_needed * strawberries_cost_per_package
    total_raspberry_cost = raspberries_packages_needed * raspberries_cost_per_package
    total_cream_cost = cream_containers_needed * cream_cost_per_container
    total_cost = total_strawberry_cost + total_raspberry_cost + total_cream_cost
    result = total_cost
    return result

print(solution())