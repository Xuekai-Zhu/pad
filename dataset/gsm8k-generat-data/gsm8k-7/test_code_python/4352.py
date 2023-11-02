def solution():
    num_tables = 20
    linen_rental_cost = 25
    place_setting_rental_cost = 10
    roses_cost = 5
    lilies_cost = 4

    # Calculate the total cost of the linen tablecloths
    total_linen_cost = num_tables * linen_rental_cost

    # Calculate the total cost of the place settings
    total_place_setting_cost = num_tables * 4 * place_setting_rental_cost

    # Calculate the total cost of the centerpieces
    total_roses_cost = num_tables * 10 * roses_cost
    total_lilies_cost = num_tables * 15 * lilies_cost
    total_centerpiece_cost = total_roses_cost + total_lilies_cost

    # Calculate the total cost of all decorations
    total_cost = total_linen_cost + total_place_setting_cost + total_centerpiece_cost
    result = total_cost
    return result

print(solution())