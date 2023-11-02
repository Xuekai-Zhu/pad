def solution():
    patrons_by_car = 12
    patrons_by_bus = 27
    capacity_per_cart = 3
    carts_needed_by_car = math.ceil(patrons_by_car / capacity_per_cart)
    carts_needed_by_bus = math.ceil(patrons_by_bus / capacity_per_cart)
    total_carts_needed = carts_needed_by_car + carts_needed_by_bus
    result = total_carts_needed
    return result

print(solution())