def solution():
    """A busy port has 4 cruise ships and twice as many cargo ships. The number of sailboats is 6 more than the cargo ships and seven times more than fishing boats. How many vessels are there on the water?"""
    cruise_ships = 4
    cargo_ships = 2 * cruise_ships
    fishing_boats = cargo_ships // 7
    sailboats = cargo_ships + 6
    total_vessels = cruise_ships + cargo_ships + fishing_boats + sailboats
    result = total_vessels
    return result

print(solution())