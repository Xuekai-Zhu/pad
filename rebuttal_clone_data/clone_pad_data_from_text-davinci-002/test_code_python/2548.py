def solution():
    cruise_ships = 4
    cargo_ships = cruise_ships / 2
    sailboats = cargo_ships + 6
    fishing_boats = cargo_ships / 7
    total_vessels = cruise_ships + cargo_ships + sailboats + fishing_boats
    result = total_vessels
    return result

print(solution())