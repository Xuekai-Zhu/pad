def solution():
    # Calculate the cost of renting tablecloths and place settings for 20 tables
    tablecloth_cost = 25 * 20
    place_setting_cost = 10 * 4 * 20
    total_rental_cost = tablecloth_cost + place_setting_cost

    # Calculate the cost of the centerpieces for 20 tables
    roses_cost = 10 * 5 * 20
    lilies_cost = 15 * 4 * 20
    total_centerpiece_cost = roses_cost + lilies_cost

    # Calculate the total cost of the decorations
    total_cost = total_rental_cost + total_centerpiece_cost
    result = total_cost
    return result

print(solution())