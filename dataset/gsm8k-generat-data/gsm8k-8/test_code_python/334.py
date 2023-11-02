def solution():
    # Calculate the cost for the strawberries
    strawberry_cups = 4
    strawberry_package_cups = 2
    strawberry_packages_needed = strawberry_cups / strawberry_package_cups
    strawberry_package_cost = 3
    total_strawberry_cost = strawberry_packages_needed * strawberry_package_cost

    # Calculate the cost for the raspberries
    raspberry_cups = 4
    raspberry_package_cups = 2
    raspberry_packages_needed = raspberry_cups / raspberry_package_cups
    raspberry_package_cost = 5
    total_raspberry_cost = raspberry_packages_needed * raspberry_package_cost

    # Calculate the cost for the cream
    cream_cups = 2
    cream_container_cups = 4
    cream_containers_needed = cream_cups / cream_container_cups
    cream_container_cost = 4
    total_cream_cost = cream_containers_needed * cream_container_cost

    # Calculate the total cost
    total_cost = total_strawberry_cost + total_raspberry_cost + total_cream_cost
    result = total_cost
    return result

print(solution())