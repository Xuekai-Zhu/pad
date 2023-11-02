def solution():
    total_bottle_caps = 100  # Jude has 100 bottle caps
    trucks_bought = 10  # Jude buys 10 trucks from Arthur
    bottle_caps_spent_on_trucks = trucks_bought * 6  # Each truck costs 6 bottle caps

    # Calculate the remaining number of bottle caps Jude has
    remaining_bottle_caps = total_bottle_caps - bottle_caps_spent_on_trucks

    # Calculate the number of cars Jude can buy with 75% of his remaining bottle caps
    cars_bought = int(0.75 * remaining_bottle_caps / 5)

    # Calculate the total number of matchbox vehicles Jude buys
    total_vehicles = trucks_bought + cars_bought
    result = total_vehicles
    return result

print(solution())