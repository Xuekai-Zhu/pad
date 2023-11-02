def solution():
    """A busy port has 4 cruise ships and twice as many cargo ships. The number of sailboats is 6 more than the cargo ships and seven times more than fishing boats. How many vessels are there on the water?"""
    # Define the number of cruise ships
    cruise_ships = 4

    # Define the number of cargo ships
    cargo_ships = 2 * cruise_ships

    # Define the number of sailboats
    sailboats = cargo_ships + 6

    # Define the number of fishing boats
    fishing_boats = sailboats / 7

    # Calculate the total number of vessels
    total_vessels = cruise_ships + cargo_ships + sailboats + fishing_boats

    # Display the total number of vessels
    result = total_vessels
    return result

print(solution())