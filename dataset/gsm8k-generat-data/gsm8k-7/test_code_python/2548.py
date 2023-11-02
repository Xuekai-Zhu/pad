def solution():
    num_cruise_ships = 4
    num_cargo_ships = num_cruise_ships * 2
    num_sailboats = num_cargo_ships + 6
    num_fishing_boats = num_sailboats // 7
    total_vessels = num_cruise_ships + num_cargo_ships + num_sailboats + num_fishing_boats
    result = total_vessels
    return result

print(solution())