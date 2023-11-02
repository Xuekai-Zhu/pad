def solution():
    cups_of_berries_per_quart = 4
    cups_of_cream_per_quart = 2

    strawberry_berrie_price = 3.0
    raspberry_berrie_price = 5.0
    cream_price = 4.0

    # Calculate the total cost of berries needed for both flavors
    total_strawberry_berrie_cost = (cups_of_berries_per_quart / 2) * strawberry_berrie_price
    total_raspberry_berrie_cost = (cups_of_berries_per_quart / 2) * raspberry_berrie_price
    total_berrie_cost = total_strawberry_berrie_cost + total_raspberry_berrie_cost

    # Calculate the total cost of cream needed for both flavors
    total_cream_cost = (cups_of_cream_per_quart * 2 / 4) * cream_price

    # Calculate the total cost of making both flavors
    total_cost = total_berrie_cost + total_cream_cost
    result = total_cost
    return result

print(solution())