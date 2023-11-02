def solution():
    """A busy port has 4 cruise ships and twice as many cargo ships. The number of sailboats is 6 more than the cargo ships and seven times more than fishing boats. How many vessels are there on the water?"""
    # Define the number of cruise ships and the multiplier for cargo ships
    cruise_ships = 4
    cargo_multiplier = 2

    # Calculate the number of cargo ships
    cargo_ships = cruise_ships * cargo_multiplier

    # Calculate the number of fishing boats
    fishing_boats = cargo_ships / 7

    # Calculate the number of sailboats
    sailboats = cargo_ships + 6

    # Calculate the total number of vessels
    total_vessels = cruise_ships + cargo_ships + fishing_boats + sailboats

    result = total_vessels
    return result

print(solution())